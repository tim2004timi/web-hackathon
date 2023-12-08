"""
Модуль с классами для редактирования админ панели
"""
import copy

from django.contrib import admin
from django.contrib.auth.models import Group

from .forms import *
from .models import Seller, Operator, CallAssistant


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = ["seller"]


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "article", "size", "color", "numbers", "seller", "time_created", "status", "delivery")
    search_fields = ["article", "name", "size", "color", "numbers", "status"]

    # def get_form(self, request, obj=None, form=None, **kwargs):
    #     form = copy.deepcopy(ProductAdminForm)
    #     if not request.user.is_superuser:
    #         print(type(form.base_fields["seller"]))
    #         # form.base_fields["seller"] = get_users.get_seller(request.user)
    #
    #         # form.base_fields["seller"].widget = HiddenInput()
    #         form.base_fields["seller"].initial = get_users.get_seller(request.user)
    #         print(type(form.base_fields["seller"].initial), form.base_fields["seller"].initial)
    #
    #     return form

    def save_model(self, request, obj, form, change):
        obj.seller = request.user.seller
        super().save_model(request, obj, form, change)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("product", "seller", "address", "date", "driver_fio", "label", "marketplace_barcode", "wrapper_barcode", "bill")
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
