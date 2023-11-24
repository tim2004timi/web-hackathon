from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from fulfillmentapp.management.commands.bot import send_registration_request
import asyncio

from .models import Product
from .pass_tests import *


def home_page_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = f"Новая заявка!\n\tНомер: {phone_number}\n\tПочта: {email}\n\tИмя: {name}"
        asyncio.run(send_registration_request(message))
        print(f"[INFO] {message}")
    return render(request=request, template_name="fulfillmentapp/index.html")


def login_page_view(request):
    if request.method == "GET":
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return redirect("/admin/")
            try:
                _ = user.seller
                return redirect('main')
            except Exception:
                pass
            try:
                _ = user.operator
                return redirect('operator')
            except Exception:
                pass

        return render(request, template_name="fulfillmentapp/login.html")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"[INFO] Попытка входа\n\tЛогин: {username}\n\tПароль: {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f"[INFO] Пользователь вошел")
            if user.is_superuser:
                return redirect('/admin/')
            elif check_is_seller(user):
                return redirect('main')
            elif check_is_operator(user):
                return redirect('operator')

            return HttpResponse("<h1>Пользователь не найден</h1>")

        else:
            data = {"error": True}
            return render(request, template_name="fulfillmentapp/login.html", context=data)


@user_passes_test(check_is_seller, login_url="/login/")
def main_page_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        numbers = request.POST.get("numbers")
        color = request.POST.get("color")
        size = request.POST.get("size")
        status = "В пути до нас"
        seller = request.user.seller

        Product.objects.create(name=name, numbers=numbers, color=color, size=size, status=status, seller=seller)

    products = Product.objects.filter(seller=request.user.seller)
    data = {
        "products": products
    }
    return render(request=request, template_name="fulfillmentapp/main.html", context=data)


@user_passes_test(check_is_operator, login_url="/login/")
def operator_page_view(request):
    products = Product.objects.all()
    data = {
        "products": products
    }
    return render(request=request, template_name="fulfillmentapp/operator.html", context=data)


def logout_page_view(request):
    logout(request)
    return redirect("home")
