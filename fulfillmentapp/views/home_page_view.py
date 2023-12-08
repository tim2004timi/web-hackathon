import asyncio

from django.http import HttpRequest
from django.shortcuts import render
from telegram.error import NetworkError

from fulfillmentapp.management.commands.bot import send_registration_request


def home_page_view(request: HttpRequest):
    """View главной страницы index.html"""

    if request.method == 'POST':

        # Получаем данные с формы заявки на регистрацию
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        name = request.POST.get('name')

        message = f"Новая заявка!\n\tНомер: {phone_number}\n\tПочта: {email}\n\tИмя: {name}"

        # Отправка сообщения заявки в telegram бот
        try:
            asyncio.run(send_registration_request(message))
            print(f"[INFO] {message}")
        except (TimeoutError, NetworkError) as e:
            print(f"[INFO] Заявка не отправлена ({e})")

    return render(request=request, template_name="fulfillmentapp/index.html")  # Переход на index.html
