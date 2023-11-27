from typing import Type
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import (
    Application,
    filters,
    MessageHandler,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    CallbackContext,
    )
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from fulfillmentapp.models import CallAssistant
from asgiref.sync import sync_to_async
from django.db.models import Q
from functools import lru_cache
import logging
from .auth_user import auth_handle
from .db_queries_wrapper import get_assistants_chat_ids
from .menu import bot_menu
import logging
# Логирование заявок на регистрацию
logger = logging.getLogger("bot.events")

bot = Bot(token=settings.TOKEN)

async def send_registration_request(message: str) -> None:
    assistants_chat_ids = await get_assistants_chat_ids()
    
    logger.info(f"New registration request was sent to call center:\n\t{message}")
    
    for chat_id in assistants_chat_ids:
        await bot.send_message(chat_id=chat_id, text=message)


@lru_cache(maxsize=None)
async def send_notification(message: str, chat_id: str) -> None:
    await bot.send_message(chat_id=chat_id, text=message)
    

class Command(BaseCommand):
    def handle(self, *args, **options):
        application = Application.builder().token(settings.TOKEN).build()
        bot_main_menu = bot_menu()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auth_handle))
        application.add_handler(CommandHandler("start", auth_handle))
    
        application.add_handler(bot_main_menu.conv_handler)
        application.run_polling(allowed_updates=Update.ALL_TYPES)
