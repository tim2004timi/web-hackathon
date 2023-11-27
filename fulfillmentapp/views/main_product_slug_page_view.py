from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render, redirect

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.models import Product, Delivery


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_product_slug_page_view(request: HttpRequest, product_slug: str):
    """View карточки товара"""

    article = int(product_slug.split("-")[1])
    product = Product.objects.get(article=article)
    seller = product.seller

    if product.status == "Ожидает заявку на отгрузку":

        if request.method == "POST":

            marketplace_barcode = request.POST.get("marketplace_barcode")
            label = request.POST.get("label")

            Delivery.objects.create(product=product,
                                    seller=seller,
                                    marketplace_barcode=marketplace_barcode,
                                    label=label)

            return redirect("main-products")

        data = {
            "product": product,
            "user": {
                "name": seller.name,
                "last_name": seller.last_name
            },
        }

        return render(request=request, template_name="fulfillmentapp/cards/application.html", context=data)

    elif product.status == "Ожидает штрихкод для тары":
        data = {
            "product": product,
            "user": {
                "name": seller.name,
                "last_name": seller.last_name
            },
        }

        return render(request=request, template_name="fulfillmentapp/cards/barcode.html", context=data)

    elif product.status == "Отгружено, ожидает оплаты":

        pass
