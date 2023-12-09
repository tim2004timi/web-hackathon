from django.contrib import admin

from fulfillmentapp.admin_panels.seller_forms import ProductAdminForm, ProductTypeAdminForm, DeliveryAdminForm
from fulfillmentapp.models import Product, ProductType, Delivery


class SellerPanel(admin.AdminSite):
    """Сайт продавца"""
    site_header = 'Fast Way'
    site_title = 'Fast Way'
    index_title = 'Главная страница'


seller_panel = SellerPanel(name='seller_panel')


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


seller_panel.register(Product, ProductAdmin)
seller_panel.register(ProductType, ProductTypeAdmin)
seller_panel.register(Delivery, DeliveryAdmin)

