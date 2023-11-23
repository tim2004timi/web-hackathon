from django.core.management.base import BaseCommand 
from django.conf import settings
from telegram.ext import (
    Application,
    filters,
    ContextTypes,
    MessageHandler)
from telegram import Update

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

class Command(BaseCommand):
    help = "tg bot"
    
    def handle(self, *args, **options):
        application = Application.builder().token(settings.TOKEN).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        application.run_polling(allowed_updates=Update.ALL_TYPES)