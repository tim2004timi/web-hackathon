from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_product_slug_page_view(request: HttpRequest, product_slug: str):
    """View карточки товара"""

    article = int(product_slug.split("-")[1])
    product = Product.objects.get(article=article)
    fields = list(product.__dict__.values())[1:]
    return HttpResponse(f"<h1>{fields}</h1>")
