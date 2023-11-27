from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_operator
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_operator, login_url="/login/")
def operator_products_page_view(request: HttpRequest):
    """View главной страницы оператора со всеми товарами"""

    products = Product.objects.all()

    data = {
        "filter": "все",
        "sorting": None,
        "selected_page": "товары",
        "products": products,
    }

    return render(request=request, template_name="fulfillmentapp/operator/products.html", context=data)

