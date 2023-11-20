from django.shortcuts import render, HttpResponse

import requests


def login_page_view(request):
    if request.method == "GET":
        return render(request=request, template_name="fulfillmentapp/login.html")

    if request.method == "POST":
        try:
            # Проверка

            message = f"""[INFO] Новый пользователь вошел:
            Логин: {request.POST.get('login')}
            Пароль: {request.POST.get('password')}
            """

        except ValueError as e:
            print(e)
            return HttpResponse(f"<h2>{e}</h2>")
