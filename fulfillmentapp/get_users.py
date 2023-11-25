"""
Модуль с функциями для проверки пользователя на принадлежность к продавцу или к оператору:
    check_is_seller(user: User) -> bool
    check_is_operator(user: User) -> bool
"""
from typing import Union

from django.contrib.auth.models import User

from fulfillmentapp.models import Seller, Operator


def get_seller(user: User) -> Union[Seller, None]:
    """Функция проверки пользователя, является ли он продавцом"""
    try:
        return user.seller
    except Exception:
        return None


def get_operator(user: User) -> Union[Operator, None]:
    """Функция проверки пользователя, является ли он оператором"""
    try:
        return user.operator
    except Exception:
        return None
