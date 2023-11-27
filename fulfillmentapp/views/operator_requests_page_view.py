from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_operator
from fulfillmentapp.models import Delivery


@user_passes_test(test_func=get_operator, login_url="/login/")
def operator_requests_page_view(request: HttpRequest):
    """View страницы оператора с отгрузками"""

    deliveries = Delivery.objects.all()
    data = {
        "selected_page": "запросы на отгрузку",
        "bills": None,
    }

    return render(request=request, template_name="fulfillmentapp/operator/requests.html", context=data)
