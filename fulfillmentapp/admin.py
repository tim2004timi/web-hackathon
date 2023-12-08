"""
Модуль с классами для редактирования админ панели
"""
from typing import Any
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.db.models.query import QuerySet
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.http.request import HttpRequest
from .get_users import get_seller

from .models import Seller, Operator, Product, CallAssistant, Delivery


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = []


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "article", "size", "color", "numbers", "seller", "time_created", "status", "delivery")
    search_fields = ["article", "name", "size", "color", "numbers", "status"]
    list_filter = ["status"]
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        #Получаем набор данных конкретно для продавца, для админов и операторов набор данных не фильтруется
        if get_seller(request.user):
            return super().get_queryset(request).filter(seller=request.user.username)
        else:
            return super().get_queryset(request)

class DeliveryAdminForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ["seller"]

    def __init__(self, *args, **kwargs):
        super(DeliveryAdminForm, self).__init__(*args, **kwargs)
        # Ограничиваем выбор Product только незанятыми объектами
        try:
            self.fields['product'].queryset = Product.objects.filter(delivery__isnull=True)
        except Exception as e:
            print(e)


class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ("product", "seller", "address", "date", "driver_fio", "label", "marketplace_barcode", "wrapper_barcode", "bill")
    search_fields = ["product", "address", "date", "driver_fio"]
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        #Получаем набор данных конкретно для продавца, для админов и операторов набор данных не фильтруется
        if get_seller(request.user):
            return super().get_queryset(request).filter(seller=request.user.username)
        else:
            return super().get_queryset(request)

class SellerAdminForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ['user', "telegram_chat_id"]
        list_filter = ["status"]

class SellerAdmin(admin.ModelAdmin):
    form = SellerAdminForm
    list_display = ("name", "last_name", "username", "password", "email", "telegram", "time_signup")
    search_fields = ["name", "last_name", "username", "email", "telegram"]


class OperatorAdminForm(ModelForm):
    class Meta:
        model = Operator
        exclude = ['user']
        list_filter = ["status"]


class OperatorAdmin(admin.ModelAdmin):
    form = OperatorAdminForm
    list_display = ('username', 'password')
    search_fields = ['username']


class AssistantAdminForm(ModelForm):
    class Meta:
        model = Operator
        exclude = ['telegram_chat_id']


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
# admin.site.unregister(User)
admin.site.unregister(Group)
