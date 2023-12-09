from django.contrib import admin

from .operator_froms import ProductAdminForm, ProductTypeAdminForm, DeliveryAdminForm
from ..models import Product, ProductType, Delivery


class OperatorPanel(admin.AdminSite):
    """Сайт оператора"""
    site_header = 'Fast Way'
    site_title = 'Fast Way'
    index_title = 'Главная страница'


operator_panel = OperatorPanel(name='operator_panel')


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("product_type", "status")
    search_fields = ["product_type", "status"]
    list_filter = ["product_type", "status"]


class ProductTypeAdmin(admin.ModelAdmin):
    form = ProductTypeAdminForm
    list_display = ("name", "article")
    search_fields = ["name", "article"]
    list_filter = ["name", "article"]


class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ("address", "date", "driver_fio", "label", "marketplace_barcode",
                    "wrapper_barcode", "bill")
    search_fields = ["product", "address", "date", "driver_fio"]


operator_panel.register(Product, ProductAdmin)
operator_panel.register(ProductType, ProductTypeAdmin)
operator_panel.register(Delivery, DeliveryAdmin)
