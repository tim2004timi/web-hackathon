from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import redirect


def logout_page_view(request: HttpRequest):
    """View логаута пользователя"""

    logout(request=request)
    return redirect("home")  # Переход на index.html
