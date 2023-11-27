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

    if product.status == "В процессе подтверждения":
        pass



