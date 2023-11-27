from telegram.ext import (
    ContextTypes,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler)
from telegram import (
    Update, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup)
from typing import Type
import logging
from .db_queries_wrapper import get_products_by_telegram_chat_id

class bot_menu:
    def __init__(self):
        #Состояния описывающие верхний уровень меню
        self.START_ROUTES, self.PRODUCT_ROUTES, self.BILL_ROUTES, self.REQUEST_ROUTES = map(chr, range(4))
        #Состояния описыюващие нижний уровень меню
        self.PRODUCTS_MENU, self.BILLS_MENU, self.REQUESTS_MENU = map(chr, range(4, 7))
        #Состояния описывающие действия в нижнем уровне меню
        self.SHOW_PRODUCTS, self.ADD_PRODUCTS, self.SHOW_BILLS, self.SHOW_SHIPPING_REQUESTS = map(chr, range(7, 11))
        #Мета состояния
        self.START_OVER = map(chr, range(11, 12))
        # Короткое название для ConversationHandler.END
        self.END = ConversationHandler.END
        # Instance для логирования 
        self.logger = logging.getLogger("bot.events")
    
        self.conv_handler = ConversationHandler(
            entry_points=[CommandHandler('menu', self.show_menu)],
            states={
                self.START_ROUTES: [
                    CallbackQueryHandler(self.show_products_menu, pattern=f"^{self.PRODUCTS_MENU}$"),
                    CallbackQueryHandler(self.show_bill_menu, pattern=f"^{self.BILLS_MENU}$"),
                    CallbackQueryHandler(self.show_shipping_requests_menu, pattern=f"^{self.REQUESTS_MENU}$"),
                    CallbackQueryHandler(self.show_menu, pattern="^" + str(self.END) + "$")
                ],
                self.PRODUCT_ROUTES: [
                    CallbackQueryHandler(self.show_products_button_handler, pattern=f"^{self.SHOW_PRODUCTS}$"),
                    CallbackQueryHandler(self.show_in_progress_msg, pattern=f"^{self.ADD_PRODUCTS}$"),
                    CallbackQueryHandler(self.show_menu, pattern="^" + str(self.END) + "$")
                ],
                self.BILL_ROUTES: [
                    CallbackQueryHandler(self.show_in_progress_msg, pattern=f"^{self.SHOW_BILLS}$"),
                    CallbackQueryHandler(self.show_menu, pattern="^" + str(self.END) + "$")
                ],
                self.REQUEST_ROUTES: [
                    CallbackQueryHandler(self.show_in_progress_msg, pattern=f"^{self.SHOW_SHIPPING_REQUESTS}$"),
                    CallbackQueryHandler(self.show_menu, pattern="^" + str(self.END) + "$")
                ],
            },
            fallbacks=[CommandHandler('menu', self.show_menu)],
        )
        
    async def show_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Отображение начального состояния меню"""
        keyboard = [
            [
                InlineKeyboardButton("Продукты", callback_data=str(self.PRODUCTS_MENU)),
                InlineKeyboardButton("Запросы на отгрузку", callback_data=str(self.REQUESTS_MENU)),
            ],
            [InlineKeyboardButton("Счета", callback_data=str(self.BILLS_MENU))],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        text = "Выберите категорию:"
        
        if context.user_data.get(self.START_OVER):
            await update.callback_query.answer()
            await update.callback_query.edit_message_text(text=text, reply_markup=reply_markup)
        else:
            await update.message.reply_text(text=text, reply_markup=reply_markup)

        context.user_data[self.START_OVER] = False
        
        return self.START_ROUTES

    async def show_products_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Отображение меню продуктов"""
        keyboard = [
            [
                InlineKeyboardButton("Показать продукты", callback_data=str(self.SHOW_PRODUCTS)),
                InlineKeyboardButton("Добавить продукт", callback_data=str(self.ADD_PRODUCTS)),
            ],
            [
                InlineKeyboardButton("Назад", callback_data=str(self.END)),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.callback_query.edit_message_text("Выберите действие:", reply_markup=reply_markup)
        
        context.user_data[self.START_OVER] = True
        
        return self.PRODUCT_ROUTES

    async def show_bill_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Отображение меню счетов"""
        keyboard = [
            [
                InlineKeyboardButton("Показать мои счета", callback_data=str(self.SHOW_BILLS)),
            ],
            [
                InlineKeyboardButton("Назад", callback_data=str(self.END)),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.callback_query.edit_message_text("Выберите действие:", reply_markup=reply_markup)
        
        context.user_data[self.START_OVER] = True
        
        return self.BILL_ROUTES

    async def show_shipping_requests_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Отображение меню запросов на отгрузку"""
        keyboard = [
            [
                InlineKeyboardButton("Показать мои заросы на отгрузку", callback_data=str(self.SHOW_SHIPPING_REQUESTS)),
            ],
            [
                InlineKeyboardButton("Назад", callback_data=str(self.END)),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.callback_query.edit_message_text("Выберите действие:", reply_markup=reply_markup)
        
        context.user_data[self.START_OVER] = True
        
        return self.REQUEST_ROUTES
        
    async def show_products_button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Обработчик нажатие на кнопку 'Показать продукты'"""
        query = update.callback_query
        await query.answer()
        
        products = await get_products_by_telegram_chat_id(chat_id=query.message.chat_id)
    
        if (len(products) == 0):
            await context.bot.send_message(chat_id=query.message.chat_id, text="Нет продуктов для отображения")
            return
        
        #TODO: Более гибкий перевод на разные языки, сейчас это решение - затычка
        translation_RU = {
            "article": "Артикул",
            "name": "Название",
            "size": "Размер",
            "color": "Цвет",
            "numbers": "Количество"
        }
        
        for product in products:
            selected_pairs = list(product.items())[1:6]
            await context.bot.send_message(chat_id=query.message.chat_id, text='\n'.join(f'<b>{translation_RU[key]}</b>: <i>{value}</i>' for key, value in selected_pairs), parse_mode="HTML")
            
        self.logger.info(f"Products were sent to chat_id: {query.message.chat_id}")
        
        keyboard = [
            [
                InlineKeyboardButton("Показать продукты", callback_data=str(self.SHOW_PRODUCTS)),
                InlineKeyboardButton("Добавить продукт", callback_data=str(self.ADD_PRODUCTS)),
            ],
            [
                InlineKeyboardButton("Назад", callback_data=str(self.END)),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.callback_query.message.reply_text(text="Выберите действие:", reply_markup=reply_markup)
        
        return self.PRODUCT_ROUTES
    #TODO: реализация остальных обработчиков endpoint'ов
    async def show_in_progress_msg(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text="Эта функция находится в разработке, извините.. :(")