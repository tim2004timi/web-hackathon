from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest
from django.shortcuts import render

from fulfillmentapp.get_users import get_seller
from fulfillmentapp.models import Product


@user_passes_test(test_func=get_seller, login_url="/login/")
def main_products_page_view(request: HttpRequest):
    """View главной страницы продавца с товарами"""

    if request.method == "POST":

        # Достаем данные о новом товаре
        name = request.POST.get("name")
        numbers = request.POST.get("numbers")
        color = request.POST.get("color")
        size = request.POST.get("size")
        status = "В пути до нас"
        seller = request.user.seller

        # Создаем в БД новый товар
        Product.objects.create(name=name, numbers=numbers, color=color, size=size, status=status, seller=seller)

    seller = get_seller(user=request.user)
    data = {
        "filter": "все",
        "sorting": None,
        "selected_page": "товары",
        "products": Product.objects.filter(seller=seller),
        "user": {
            "name": seller.name,
            "last_name": seller.last_name
        },
    }

    return render(request=request, template_name="fulfillmentapp/main/products.html", context=data)
