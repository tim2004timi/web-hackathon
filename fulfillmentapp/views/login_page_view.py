from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from fulfillmentapp.get_users import get_seller, get_operator


def login_page_view(request: HttpRequest):
    """View страницы авторизации login.html"""

    if request.method == "GET":
        user = request.user

        # Проверка на аутентификацию пользователя
        if user.is_authenticated:

            if user.is_superuser:
                return redirect("/admin/")

            elif get_seller(user=user):
                return redirect('main-products')

            elif get_operator(user=user):
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

            elif get_seller(user=user):
                return redirect('main-products')

            elif get_operator(user=user):
                return redirect('operator-products')

            return HttpResponse("<h1>Пользователь не найден</h1>")

        # Если пользователь не авторизовался
        else:
            data = {"error": True}
            return render(request=request, template_name="fulfillmentapp/login.html", context=data)
