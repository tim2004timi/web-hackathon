from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_operator


@user_passes_test(test_func=get_operator, login_url="/login/")
def operator_bills_page_view(request: HttpRequest):
    """View страницы оператора со счетами"""

    data = {
        "selected_page": "счета",
        "bills": None,
    }

    return render(request=request, template_name="fulfillmentapp/operator/bills.html", context=data)
