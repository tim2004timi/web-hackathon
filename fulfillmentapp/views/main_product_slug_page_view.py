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

            delivery = Delivery.objects.create(product=product, seller=seller)
            # delivery.marketplace_barcode = delivery.label = bin(1)

            try:
                delivery.marketplace_barcode = request.FILES["marketplace_barcode"].read()
            except Exception as e:
                print(e)
            try:
                delivery.label = request.FILES["label"].read()
            except Exception:
                pass

            delivery.save()
            product.status = "В процессе подтверждения"
            product.save()

            # Тут шлется уведомление пользователю в тг !!!!!

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

        if request.method == "POST":

            delivery = product.delivery

            try:
                delivery.wrapper_barcode = request.FILES["wrapper_barcode"].read()
            except Exception as e:
                print(e)

            delivery.save()
            product.status = "В процессе подтверждения"
            product.save()

            # Тут шлется уведомление пользователю в тг

            return redirect("main-products")

        data = {
            "product": product,
            "user": {
                "name": seller.name,
                "last_name": seller.last_name
            },
        }

        return render(request=request, template_name="fulfillmentapp/cards/barcode.html", context=data)

    elif product.status == "Отгружено, ожидает оплаты":

        # Показ pdf
        pass
