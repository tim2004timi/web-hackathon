from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from fulfillmentapp.management.commands.bot import send_registration_request
import asyncio

from .models import Product
from .pass_tests import check_is_operator, check_is_seller


def home_page_view(request: HttpRequest):
    """View главной страницы index.html"""

    if request.method == 'POST':

        # Получаем данные с формы заявки на регистрацию
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        name = request.POST.get('name')

        message = f"Новая заявка!\n\tНомер: {phone_number}\n\tПочта: {email}\n\tИмя: {name}"

        # Отправка сообщения заявки в telegram бот
        asyncio.run(send_registration_request(message))

        # Вывод в консоль информации о заявке
        print(f"[INFO] {message}")

    return render(request=request, template_name="fulfillmentapp/index.html")  # Переход на index.html


def login_page_view(request: HttpRequest):
    """View страницы авторизации login.html"""

    if request.method == "GET":
        user = request.user

        # Проверка на аутентификацию пользователя
        if user.is_authenticated:

            if user.is_superuser:
                return redirect("/admin/")

            elif check_is_seller(user=user):
                return redirect('main-products')

            elif check_is_operator(user=user):
                return redirect('operator')

        return render(request=request, template_name="fulfillmentapp/login.html")  # Переход на login.html

    if request.method == 'POST':

        # Получаем данные из формы авторизации
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"[INFO] Попытка входа\n\tЛогин: {username}\n\tПароль: {password}")

        # Аутентификация пользователя в системе
        user = authenticate(request, username=username, password=password)

        # Проверка пользователя на прохождение аутентификации
        if user is not None:

            # Догин пользователя в системе
            login(request=request, user=user)

            print(f"[INFO] Пользователь вошел")

            if user.is_superuser:
                return redirect('/admin/')

            elif check_is_seller(user=user):
                return redirect('main-products')

            elif check_is_operator(user=user):
                return redirect('operator')

            return HttpResponse("<h1>Пользователь не найден</h1>")

        # Если пользователь не авторизовался
        else:
            data = {"error": True}
            return render(request=request, template_name="fulfillmentapp/login.html", context=data)


@user_passes_test(test_func=check_is_seller, login_url="/login/")
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

    products = Product.objects.filter(seller=request.user.seller)
    data = {
        "products": products
    }

    return render(request=request, template_name="fulfillmentapp/main/products.html", context=data)


@user_passes_test(test_func=check_is_operator, login_url="/login/")
def operator_page_view(request: HttpRequest):
    """View главной страницы оператора со всеми товарами"""

    products = Product.objects.all()
    data = {
        "products": products
    }
    return render(request=request, template_name="fulfillmentapp/operator.html", context=data)


@user_passes_test(test_func=check_is_seller, login_url="/login/")
def main_product_slug_page_view(request: HttpRequest, product_slug: str):
    """View карточки товара"""

    article = int(product_slug.split("-")[1])


def logout_page_view(request: HttpRequest):
    """View логаута пользователя"""

    logout(request=request)
    return redirect("home")  # Переход на index.html
