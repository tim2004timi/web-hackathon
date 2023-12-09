import asyncio

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render
from telegram.error import NetworkError

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.management.commands.bot import send_notification
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_products_page_view(request: HttpRequest, seller=None):
    """View главной страницы продавца с товарами"""

    if request.method == "POST":

        # Достаем данные о новом товаре
        name = request.POST.get("name")
        numbers = request.POST.get("numbers")
        color = request.POST.get("color")
        size_1 = request.POST.get("size_1")
        size_2 = request.POST.get("size_2")
        size_3 = request.POST.get("size_3")

        seller = request.user.seller

        size = f"{size_1}*{size_2}*{size_3}"

        # Создаем в БД новый товар
        product = Product.objects.create(name=name, numbers=numbers, color=color, size=size, seller=seller)

        # Уведомление в телеграм
        message = f"Продукт добавлен: <b>{name}</b>\nСтатус: <b>{product.status}</b>"
        try:
            asyncio.run(send_notification(message, seller.telegram_chat_id))
        except (TimeoutError, NetworkError) as e:
            print(e)

    if not seller:
        seller = get_seller(user=request.user)
    products = Product.objects.filter(seller=seller)

    data = {
        "filter": "все",
        "sorting": None,
        "selected_page": "товары",
        "products": products,
        "user": {
            "name": seller.name,
            "last_name": seller.last_name
        },
    }

    return render(request=request, template_name="fulfillmentapp/main/products.html", context=data)
