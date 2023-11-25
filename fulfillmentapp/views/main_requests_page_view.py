from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.models import Delivery


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_requests_page_view(request: HttpRequest):
    """View главной страницы продавца с отгрузками"""

    seller = get_seller(user=request.user)
    deliveries = seller.deliveries
    name = seller.name
    last_name = seller.last_name
    data = {
        "selected_page": "запросы на отгрузку",
        "bills": None,
        "user": {
            "name": name,
            "last_name": last_name
        },
    }

    return render(request=request, template_name="fulfillmentapp/main/requests.html", context=data)
