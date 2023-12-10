from django.contrib import admin
from django.utils.html import format_html

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


operator_panel.register(Product, ProductAdmin)
operator_panel.register(ProductType, ProductTypeAdmin)
operator_panel.register(Delivery, DeliveryAdmin)
