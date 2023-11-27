from asgiref.sync import sync_to_async
from django.db.models import Model, Q
from fulfillmentapp.models import CallAssistant, Seller
from django.conf import settings
from typing import Type

@sync_to_async
#TODO: закэшировать
def get_user_by_telegram(tg_username: str, model: Type[Model]) -> Model:
    """Получить объект по его telegram username """
    return model.objects.filter(telegram=tg_username).first()

@sync_to_async
def set_telegram_chat_id(user: Model, chat_id: int) -> None:
    """Изменить telegram_chat_id у пользователя"""
    user.telegram_chat_id = chat_id
    user.save()

@sync_to_async
#TODO: закэшировать
def get_telegram_chat_id(user: Model, chat_id: int) -> str:
    """Получить telegram_chat_id пользователя"""
    return user.telegram_chat_id

@sync_to_async
def get_products_by_telegram_chat_id(chat_id: str) -> list[dict[str, str]]:
    """Получить список товаров продавца по его telegram_chat_id"""
    result = []
    seller = Seller.objects.filter(telegram_chat_id=chat_id).first()
    products = seller.products
    for product in products.all():
        result.append(product.__dict__)
    return result

@sync_to_async
#TODO: закэшировать
def get_assistants_chat_ids() -> list[str]:
    """Получить список telegram_chat_id всех ассистентов"""
    query_set = CallAssistant.objects.filter(~Q(telegram_chat_id=""))
    return [item.telegram_chat_id for item in query_set]
