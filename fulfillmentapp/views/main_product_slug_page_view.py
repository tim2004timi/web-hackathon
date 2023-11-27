from datetime import datetime

from django.contrib.auth.decorators import user_passes_test
from django.db.models import DateTimeField
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.formats import date_format

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_product_slug_page_view(request: HttpRequest, product_slug: str):
    """View карточки товара 'добавить заявку' """

    article = int(product_slug.split("-")[1])
    product = Product.objects.get(article=article)

    if product.status == "Ожидает заявку на отгрузку":
        data = {
            "product": product
        }

        return render(request=request, template_name="fulfillmentapp/cards/application.html", context=data)

    elif product.status == "Ожидает штрихкод для тары":
        data = {
            "product": product
        }

        return render(request=request, template_name="fulfillmentapp/cards/barcode.html", context=data)
