from django.shortcuts import render, HttpResponse

import requests


def home_page_view(request):
    return render(request=request, template_name="fulfillmentapp/index.html")


def login_page_view(request):
    if request.method == "GET":
        return render(request=request, template_name="fulfillmentapp/login.html")

    if request.method == "POST":
        try:
            # Проверка

            message = f"[INFO] Новый пользователь вошел\n\tЛогин: {request.POST.get('login')}\n\tПароль: {request.POST.get('password')}"
            print(message)

            return render(request=request, template_name="fulfillmentapp/index.html")

        except ValueError as e:
            print(e)
            return HttpResponse(f"<h2>{e}</h2>")
