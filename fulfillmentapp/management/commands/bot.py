from django.core.management.base import BaseCommand 
from django.conf import settings
from telegram.ext import (
    Application,
    filters,
    ContextTypes,
    MessageHandler,
    CommandHandler)
from telegram import Update
from fulfillmentapp.models import Seller
from asgiref.sync import sync_to_async

@sync_to_async
def get_user_by_telegram(tg_usename: str) -> Seller:
    return Seller.objects.filter(telegram=tg_usename).first()

@sync_to_async
def set_telegram_chat_id(user: Seller, chat_id: int) -> None:
    user.telegram_chat_id = chat_id
    user.save()

async def auth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    tg_usename = message.from_user.name
    user = await get_user_by_telegram(tg_usename=tg_usename)
    
    if user:
        await set_telegram_chat_id(user=user, chat_id=message.chat_id)
        await message.reply_text(f"Теперь Вы можете получать уведомления в этот чат!")
    else:
        await message.reply_text("Вы не зарегистрированы в системе!")

class Command(BaseCommand):
    def handle(self, *args, **options):
        application = Application.builder().token(settings.TOKEN).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auth))
        application.add_handler(CommandHandler("start", auth))
        application.run_polling(allowed_updates=Update.ALL_TYPES)