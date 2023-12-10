from typing import Any

from django.contrib import admin
from django.utils.html import format_html
from django.forms import ModelForm

from .admin_forms import ProductAdminForm, SellerAdminForm, OperatorAdminForm, AssistantAdminForm, ProductTypeAdminForm, \
    DeliveryAdminForm
from ..models import Product, Operator, Seller, CallAssistant, ProductType, Delivery


class AdminPanel(admin.AdminSite):
    """Сайт админа"""
    site_header = 'Fast Way'
    site_title = 'Fast Way'
    index_title = 'Главная страница'


admin_panel = AdminPanel(name='admin_panel')


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("product_type", "status")
    search_fields = ["product_type", "status"]
    list_filter = []


class ProductTypeAdmin(admin.ModelAdmin):
    form = ProductTypeAdminForm
    list_display = ("name", "seller", "color_article", "size", "price", "available_amount")
    search_fields = ["name", "article"]
    list_filter = ["seller"]

    def color_article(self, obj):
        return format_html('<span style="color: #8615CB">{}</span>', obj.article)

    def available_amount(self, obj):
        amount = Product.objects.filter(product_type=obj).count()
        return amount

    color_article.short_description = "Артикул"
    available_amount.short_description = "Доступно"


class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ("address", "date", "driver_fio", "label", "marketplace_barcode",
                    "wrapper_barcode", "bill")
    search_fields = ["product", "address", "date", "driver_fio"]


class SellerAdmin(admin.ModelAdmin):
    form = SellerAdminForm
    list_display = ("name", "last_name", "username", "password", "email", "telegram", "time_signup")
    search_fields = ["name", "last_name", "username", "email", "telegram"]


class OperatorAdmin(admin.ModelAdmin):
    form = OperatorAdminForm
    list_display = ('username', 'name', 'last_name', 'email')
    search_fields = ['username', 'name', 'last_name']


class AssistantAdmin(admin.ModelAdmin):
    form = AssistantAdminForm
    list_display = ('telegram',)
    search_fields = ['telegram']


admin_panel.register(Operator, OperatorAdmin)
admin_panel.register(Seller, SellerAdmin)
admin_panel.register(CallAssistant, AssistantAdmin)
admin_panel.register(Product, ProductAdmin)
admin_panel.register(ProductType, ProductTypeAdmin)
admin_panel.register(Delivery, DeliveryAdmin)



