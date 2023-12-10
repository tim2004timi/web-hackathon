from django.contrib import admin
from django.utils.html import format_html

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
    list_filter = []
    autocomplete_fields = ("status",)

    def save_model(self, request, obj, form, change):
        # Устанавливаем seller из текущего пользователя при создании объекта
        obj.seller = request.user.seller
        obj.save()


class ProductTypeAdmin(admin.ModelAdmin):
    form = ProductTypeAdminForm
    list_display = ("name", "color_article", "size", "price", "available_amount")
    search_fields = ["name", "article"]
    list_filter = []

    def save_model(self, request, obj, form, change):
        # Устанавливаем seller из текущего пользователя при создании объекта
        obj.seller = request.user.seller
        obj.save()

    def color_article(self, obj):
        return format_html('<span style="color: #8615CB">{}</span>', obj.article)

    def available_amount(self, obj):
        amount = Product.objects.filter(product_type=obj).count()
        return amount

    color_article.short_description = "Артикул"
    available_amount.short_description = "Доступно"


class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ("name", "address", "date", "driver_fio", "label", "marketplace_barcode",
                    "wrapper_barcode", "bill")
    search_fields = ["product", "address", "date", "driver_fio"]
    autocomplete_fields = ("product_type", )

    def save_model(self, request, obj, form, change):
        # Устанавливаем seller из текущего пользователя при создании объекта
        obj.seller = request.user.seller
        obj.save()

    def name(self, obj):
        return obj

    name.short_description = "Название"


seller_panel.register(Product, ProductAdmin)
seller_panel.register(ProductType, ProductTypeAdmin)
seller_panel.register(Delivery, DeliveryAdmin)

