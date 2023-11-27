import asyncio

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render, redirect

from fulfillmentapp.get_users import get_operator
from fulfillmentapp.models import Product, Delivery
from telegram.error import NetworkError

from fulfillmentapp.management.commands.bot import send_notification


@user_passes_test(test_func=get_operator, login_url="/login/")
def operator_product_slug_page_view(request: HttpRequest, product_slug: str):
    """View карточки товара"""

    article = int(product_slug.split("-")[1])
    product = Product.objects.get(article=article)
    seller = product.seller

    if product.status == "В пути до нас":
        product.status = "Ожидает заявку на отгрузку"
        product.save()

        # Отправка сообщения заявки в telegram бот
        message = f"Продукт: <b>{product}</b>\nИзмененный статус: <b>{product.status}</b>"
        try:
            asyncio.run(send_notification(message, seller.telegram_chat_id))
        except (TimeoutError, NetworkError) as e:
            print(e)

        return redirect("operator-products")

    elif product.status == "В процессе подтверждения":

        if request.method == "POST":
            pass

        data = {
            "product": product
        }

        return render(request=request, template_name="fulfillmentapp/cards/data_card.html", context=data)




