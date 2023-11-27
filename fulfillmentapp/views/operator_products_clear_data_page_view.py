from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_operator
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_operator, login_url="/login/")
def operator_products_clear_data_page_view(request: HttpRequest, **kwargs):
    """View страницы оператора с фильтром и сортировкой"""

    # Достаем товары продавцов (заказчиков)
    products = Product.objects.all()

    status = kwargs["filter"]
    sorting = kwargs["sorting"]

    # Фильтр товаров
    if status and status != "все":
        if status == "в пути":
            new_status = "в пути до нас"
        elif status == "ожидает штрихкод":
            new_status = "ожидает штрихкод для тары"
        elif status == "ожидает заявку на отгрузку":
            new_status = "ожидает заявку на отгрузку"
        else:
            new_status = "отгружено, ожидает оплаты"
        products = products.filter(status=new_status.capitalize())

    # Сортировка товаров
    if sorting != "None":
        if sorting == "time_created":
            products = products.order_by(f"-{sorting}")
        else:
            products = products.order_by(sorting)

    data = {
        "filter": status,
        "sorting": sorting,
        "selected_page": "товары",
        "products": products,
    }

    return render(request=request, template_name="fulfillmentapp/operator/products.html", context=data)
