from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_seller


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_bills_page_view(request: HttpRequest):
    """View главной страницы продавца со счетами"""

    seller = get_seller(user=request.user)
    name = seller.name
    last_name = seller.last_name
    data = {
        "bills": None,
        "user": {
            "name": name,
            "last_name": last_name
        },
    }

    return render(request=request, template_name="fulfillmentapp/main/bills.html", context=data)
