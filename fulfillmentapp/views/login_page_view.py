import requests
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

import setting_secrets
from fulfillmentapp.get_users import get_seller, get_operator

import os
from dotenv import load_dotenv

load_dotenv(".env.app")

def login_page_view(request: HttpRequest):
    """View страницы авторизации login.html"""

    # Ключ для reCAPTCHA
    recaptcha_site_key = {"site_key": os.getenv("RECAPTCHA_SITE_KEY")}

    if request.method == "GET":
        user = request.user

        # Проверка на аутентификацию пользователя
        if user.is_authenticated:

            if user.is_superuser:
                return redirect("/admin/")

            elif get_seller(user=user):
                return redirect('main-products')

            elif get_operator(user=user):
                return redirect('operator-products')

        return render(request=request, template_name="fulfillmentapp/login.html", context=recaptcha_site_key)

    if request.method == 'POST':

        # Верификация reCAPTCHA
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': os.getenv("RECAPTCHA_SECRET_KEY"),
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        # if not result['success']:
        #     return HttpResponse("<h1>Извините, замечены подозрительные действия. Попробуйте еще раз</h1>")

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

            elif get_seller(user=user):
                # return redirect('main-products')
                return redirect('/admin/')

            elif get_operator(user=user):
                return redirect('operator-products')

            return HttpResponse("<h1>Пользователь не найден</h1>")

        # Если пользователь не авторизовался
        else:
            data = {
                "error": True,
                **recaptcha_site_key
            }

            return render(request=request, template_name="fulfillmentapp/login.html", context=data)
