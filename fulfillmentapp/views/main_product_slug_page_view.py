from datetime import datetime

from django.contrib.auth.decorators import user_passes_test
from django.db.models import DateTimeField
from django.http import HttpRequest, HttpResponse
from django.utils.formats import date_format

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_product_slug_page_view(request: HttpRequest, product_slug: str):
    """View карточки товара"""

    article = int(product_slug.split("-")[1])
    product = Product.objects.get(article=article)
    fields = list(product.__dict__.values())[1:]
    print(type(fields[-1]))
    fields = list(map(lambda x: date_format(x) if type(x) == datetime else str(x), fields))
    return HttpResponse(f"<h1>{' '.join(fields)}</h1>")
