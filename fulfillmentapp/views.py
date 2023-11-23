from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect


from fulfillmentapp.forms import AuthenticationForm


def home_page_view(request):
    return render(request=request, template_name="fulfillmentapp/index.html")


def login_page_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("main")

        form = AuthenticationForm()
        return render(request, template_name="fulfillmentapp/login.html", context={'form': form})
        # return render(request=request, template_name="fulfillmentapp/login.html")

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(f"[INFO] Попытка входа\n\tЛогин: {username}\n\tПароль: {password}")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # if status == "Админ":
                #     return redirect('/admin/')
                # Редирект на нужную страницу после входа
                return redirect('main')
            else:
                # Обработка неверных данных
                return HttpResponse("<h2>Неверный пароль</h2>")

        # message = f"[INFO] Новый пользователь вошел\n\tЛогин: {request.POST.get('login')}\n\tПароль: {request.POST.get('password')}"
        # print(message)

        # return render(request=request, template_name="fulfillmentapp/index.html")


def main_page_view(request):
    return render(request=request, template_name="fulfillmentapp/main.html")

def logout_page_view(request):
    logout(request)
    return redirect("home")
