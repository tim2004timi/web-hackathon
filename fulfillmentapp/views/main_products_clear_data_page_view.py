from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_products_clear_data_page_view(request: HttpRequest, seller=None, **kwargs):
    """View главной страницы с фильтром и сортировкой"""

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
        Product.objects.create(name=name, numbers=numbers, color=color, size=size, seller=seller)

    # Достаем товары продавца (заказчика)
    if not seller:
        seller = get_seller(user=request.user)
    products = Product.objects.filter(seller=seller)

    status = kwargs["filter"]
    sorting = kwargs["sorting"]

    # Фильтр товаров
    if status and status != "все":
        new_status = status.capitalize()
        if status == "в пути":
            new_status += " до нас"
        products = products.filter(status=new_status)

    # Сортировка товаров
    if sorting != "None":
        if sorting == "time_created":
            products = products.order_by(f"-{sorting}")
        else:
            products = products.order_by(sorting)

    data = {
        "filter": status,
        "sorting": sorting,
        "selected_page": "товары",
        "products": products,
        "user": {
            "name": seller.name,
            "last_name": seller.last_name
        },
    }

    return render(request=request, template_name="fulfillmentapp/main/products.html", context=data)
