"""
Модуль с классами для редактирования админ панели
"""
from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.contrib.auth.models import Group, User
from django.http.request import HttpRequest
from django.utils.html import format_html

from .get_users import get_seller

from .forms import *
from .models import Seller, Operator, CallAssistant


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "article", "color", "numbers", "seller", "colored_status", "delivery")
    search_fields = ["article", "name", "size", "color", "numbers", "status"]
    list_filter = ["status"]

    def colored_status(self, obj):
        # Замените 'В пути до нас' на тот статус, который вам нужно выделить красным
        return format_html('<span style="{}">{}</span>', obj.get_button_style(), obj.status)

    colored_status.short_description = 'Статус'

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        # Получаем набор данных конкретно для продавца, для админов и операторов набор данных не фильтруется
        if get_seller(request.user):
            return super().get_queryset(request).filter(seller=request.user.username)
        else:
            return super().get_queryset(request)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("product", "seller", "address", "date", "driver_fio", "label", "marketplace_barcode",
                    "wrapper_barcode", "bill")
    search_fields = ["product", "address", "date", "driver_fio"]

    def get_form(self, request, obj=None, form=None, **kwargs):
        if request.user.is_superuser:
            form = DeliveryAdminForm
        elif obj.product.status == "Ожидает заявку на отгрузку":
            form = AdminWaitingDeliveryForm
        elif obj.product.status == "В процессе подтверждения":
            form = AdminWaitingConfirmForm
        elif obj.product.status == "Ожидает штрихкод для тары":
            form = AdminWaitingWrapperBarcodeForm
        return form
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        # Получаем набор данных конкретно для продавца, для админов и операторов набор данных не фильтруется
        if get_seller(request.user):
            return super().get_queryset(request).filter(seller=request.user.username)
        else:
            return super().get_queryset(request)


class SellerAdmin(admin.ModelAdmin):
    form = SellerAdminForm
    list_display = ("name", "last_name", "username", "password", "email", "telegram", "time_signup")
    search_fields = ["name", "last_name", "username", "email", "telegram"]


class OperatorAdmin(admin.ModelAdmin):
    form = OperatorAdminForm
    list_display = ('username', 'password')
    search_fields = ['username']


class AssistantAdmin(admin.ModelAdmin):
    form = AssistantAdminForm
    list_display = ('telegram',)
    search_fields = ['telegram']


# Добавляем модели на админ модель
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(CallAssistant, AssistantAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Delivery, DeliveryAdmin)

# Убираем модель User и Group
admin.site.unregister(User)
admin.site.unregister(Group)
