"""
Модуль с классами для редактирования админ панели
"""
from django.contrib import admin
from django.forms import ModelForm
from django.contrib.auth.models import User, Group

import copy

from .models import Seller, Operator, Product, CallAssistant, Delivery


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = []


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "article", "size", "color", "numbers", "seller", "time_created", "status", "delivery")
    search_fields = ["article", "name", "size", "color", "numbers", "status"]


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
    # form = DeliveryAdminForm
    list_display = ("product", "seller", "address", "date", "driver_fio", "label", "marketplace_barcode", "wrapper_barcode", "bill")
    search_fields = ["product", "address", "date", "driver_fio"]

    def get_form(self, request, obj=None, form=None, **kwargs):

        # form.base_fields["first_name"].label = "First Name (Humans only!):"
        if obj.product.status == "Ожидает заявку на отгрузку":
            form = copy.deepcopy(DeliveryAdminForm)
            form.Meta.exclude += ["label", "marketplace_barcode", "wrapper_barcode", "bill"]
        print(type(obj), obj)
        return form


class SellerAdminForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ['user', "telegram_chat_id"]


class SellerAdmin(admin.ModelAdmin):
    form = SellerAdminForm
    list_display = ("name", "last_name", "username", "password", "email", "telegram", "time_signup")
    search_fields = ["name", "last_name", "username", "email", "telegram"]


class OperatorAdminForm(ModelForm):
    class Meta:
        model = Operator
        exclude = ['user']


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
