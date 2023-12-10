from telegram.ext import (
    ContextTypes,)
from telegram import Update
from fulfillmentapp.models import Seller, CallAssistant
from asgiref.sync import sync_to_async
from django.db.models import Model
from functools import lru_cache
from django.conf import settings
from typing import Type
from .db_queries_wrapper import get_user_by_telegram, set_telegram_chat_id, get_telegram_chat_id
import logging

logger = logging.getLogger("bot.events")

#TODO: Добавить кэширование
async def auth_handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Метод обрабатывающий запрос (в данный реализации это каждое новое сообщение) на авторизацию пользователя в системе"""
    message = update.message
    tg_username = message.from_user.name
    
    if user := await get_user_by_telegram(tg_username=tg_username, model=Seller) or await get_user_by_telegram(tg_username=tg_username, model=CallAssistant):
        await auth_user(user=user, update=update, message_if_first_auth="Теперь вы авторизированы!")
    else:
        await message.reply_text("Вы не зарегистрированы в системе!")


async def auth_user(user: Model, update: Update, message_if_first_auth: str) -> None:
    """Метод реализующий авторизацию пользователя в системе"""
    message = update.message
    
    if not await get_telegram_chat_id(user=user, chat_id=message.chat_id):
        await set_telegram_chat_id(user=user, chat_id=message.chat_id)
        await message.reply_text(message_if_first_auth)
        
async def check_auth(update: Update) -> bool:
    """Проверка авторизации пользователя"""
    message = update.message
    if not await get_user_by_telegram(tg_username=message.from_user.name, model=Seller):
        await message.reply_text("Вы не авторизированы в системе!")
        return False
    return True