"""
Модуль с функциями для проверки пользователя на принадлежность к продавцу или к оператору:
    check_is_seller(user: User) -> bool
    check_is_operator(user: User) -> bool
"""

from django.contrib.auth.models import User


def check_is_seller(user: User) -> bool:
    """Функция проверки пользователя, является ли он продавцом"""
    try:
        _ = user.seller
        return True
    except Exception:
        return False


def check_is_operator(user: User) -> bool:
    """Функция проверки пользователя, является ли он оператором"""
    try:
        _ = user.operator
        return True
    except Exception:
        return False
