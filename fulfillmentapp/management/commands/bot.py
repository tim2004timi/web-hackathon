from typing import Type

from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import (
    Application,
    filters,
    ContextTypes,
    MessageHandler,
    CommandHandler)
from telegram import Update, Bot
from fulfillmentapp.models import Seller, CallAssistant
from asgiref.sync import sync_to_async
from django.db.models import Model, Q
from functools import lru_cache
import logging


# Логирование заявок на регистрацию
logger = logging.getLogger("bot.events")

@sync_to_async
@lru_cache(maxsize=None)
def get_assistants_chat_ids() -> list[str]:
    query_set = CallAssistant.objects.filter(~Q(telegram_chat_id=""))
    return [item.telegram_chat_id for item in query_set]

@sync_to_async
@lru_cache(maxsize=None)
def get_user_by_telegram(tg_username: str, model: Type[Model]) -> Model:
    return model.objects.filter(telegram=tg_username).first()

@sync_to_async
def set_telegram_chat_id(user: Model, chat_id: int) -> None:
    user.telegram_chat_id = chat_id
    user.save()

@sync_to_async
@lru_cache(maxsize=None)
def get_telegram_chat_id(user: Model, chat_id: int) -> str:
    return user.telegram_chat_id


async def send_registration_request(message: str) -> None:
    assistants_chat_ids = await get_assistants_chat_ids()
    print("[INFO] Заявка отправлена в колл центр")
    logger.info(f"New registration request was sent to call center:\n\t{message}")
    bot = Bot(token=settings.TOKEN)
    for chat_id in assistants_chat_ids:
        await bot.send_message(chat_id=chat_id, text=message)


async def auth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    tg_username = message.from_user.name
    if user := await get_user_by_telegram(tg_username=tg_username, model=Seller) or await get_user_by_telegram(tg_username=tg_username, model=CallAssistant):
        await auth_user(user=user, update=update, message_if_first_auth="Теперь вы авторизированы!")
    else:
        await message.reply_text("Вы не зарегистрированы в системе!")


async def auth_user(user: Model, update: Update, message_if_first_auth: str) -> None:
    message = update.message
    if not await get_telegram_chat_id(user=user, chat_id=message.chat_id):
        await set_telegram_chat_id(user=user, chat_id=message.chat_id)
        await message.reply_text(message_if_first_auth)


class Command(BaseCommand):
    def handle(self, *args, **options):
        application = Application.builder().token(settings.TOKEN).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auth))
        application.add_handler(CommandHandler("start", auth))
        application.run_polling(allowed_updates=Update.ALL_TYPES)
