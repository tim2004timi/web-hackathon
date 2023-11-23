from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from fulfillmentapp.management.commands.bot import send_registration_request
import asyncio

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
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect("/admin/")
            return redirect("main")
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
            return redirect('main')
        else:
            data = {"error": True}
            return render(request, template_name="fulfillmentapp/login.html", context=data)


def main_page_view(request):
    return render(request=request, template_name="fulfillmentapp/main.html")


def logout_page_view(request):
    logout(request)
    return redirect("home")
