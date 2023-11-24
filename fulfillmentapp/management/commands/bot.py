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


bot = Bot(token=settings.TOKEN)


@sync_to_async
def get_assistants_chat_ids() -> list[str]:
    query_set = CallAssistant.objects.filter(~Q(telegram_chat_id=""))
    return [item.telegram_chat_id for item in query_set]


@sync_to_async
def get_user_by_telegram(tg_usename: str, model: Type[Model]) -> Model:
    return model.objects.filter(telegram=tg_usename).first()


@sync_to_async
def set_telegram_chat_id(user: Model, chat_id: int) -> None:
    user.telegram_chat_id = chat_id
    user.save()


async def send_registration_request(message: str) -> None:
    assistants_chat_ids = await get_assistants_chat_ids()
    print("[INFO] Заявка отправлена в колл центр")
    for chat_id in assistants_chat_ids:
        await bot.send_message(chat_id=chat_id, text=message)


async def auth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    tg_username = message.from_user.name
    if user := await get_user_by_telegram(tg_usename=tg_username, model=Seller):
        await auth_sellers(user=user, update=update)
        await message.reply_text(f"Теперь Вы можете получать уведомления в этот чат!")
    elif user := await get_user_by_telegram(tg_usename=tg_username, model=CallAssistant):
        await auth_assistants(user=user, update=update)
        await message.reply_text(f"Теперь Вы можете получать заявки в этот чат!")
    else:
        await message.reply_text("Вы не зарегистрированы в системе!")


async def auth_assistants(user: Model, update: Update) -> None:
    message = update.message
    await set_telegram_chat_id(user=user, chat_id=message.chat_id)


async def auth_sellers(user: Model, update: Update) -> None:
    message = update.message
    await set_telegram_chat_id(user=user, chat_id=message.chat_id)


class Command(BaseCommand):
    def handle(self, *args, **options):
        application = Application.builder().token(settings.TOKEN).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auth))
        application.add_handler(CommandHandler("start", auth))
        application.run_polling(allowed_updates=Update.ALL_TYPES)
