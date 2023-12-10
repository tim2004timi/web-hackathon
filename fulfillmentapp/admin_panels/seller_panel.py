from copy import deepcopy

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from fulfillmentapp.admin_panels.seller_forms import ProductAdminForm, ProductTypeAdminForm, WaitingDeliveryAdminForm
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

    def save_model(self, request, obj, form, change):
        # Устанавливаем seller из текущего пользователя при создании объекта
        obj.seller = request.user.seller
        obj.save()


class ProductTypeAdmin(admin.ModelAdmin):
    form = ProductTypeAdminForm
    list_display = ("style_name", "style_article", "style_size", "style_price", "style_amount")
    search_fields = ["name", "article"]
    list_filter = []

    def save_model(self, request, obj, form, change):
        # Устанавливаем seller из текущего пользователя при создании объекта
        obj.seller = request.user.seller
        obj.save()

    def style_name(self, obj):
        return format_html('<span style="font-size: 14px; height: 100px">{}</span>', obj.name)
    
    def style_article(self, obj):
        return format_html('<span style="color: #8615CB; font-size: 14px; height: 100px">{}</span>', obj.article)
    
    def style_size(self, obj):
        return format_html('<span style="color: #8615CB; font-size: 14px; height: 100px">{}</span>', obj.size)

    def style_price(self, obj):
        return format_html('<span style="color: #8615CB; font-size: 14px; height: 100px">{}</span>', obj.price)

    def style_amount(self, obj):
        amount = Product.objects.filter(product_type=obj).count()
        return format_html('<span style="color: #8615CB; font-size: 14px; height: 100px">{}</span>', amount)

    style_name.short_description = "Название"
    style_article.short_description = "Артикул"
    style_size.short_description = 'Размер'
    style_price.short_description = 'Цена'
    style_amount.short_description = "Доступно"


class DeliveryAdmin(admin.ModelAdmin):
    form = WaitingDeliveryAdminForm
    list_display = ("name", "address", "date", "driver_fio", "label", "marketplace_barcode",
                    "wrapper_barcode", "bill")
    search_fields = ["product", "address", "date", "driver_fio"]
    autocomplete_fields = ("product_type",)

    def save_model(self, request, obj, form, change):
        # Устанавливаем seller из текущего пользователя при создании объекта
        if obj is not None:
            amount = form.cleaned_data.get("amount")
            if amount < 1 or amount > obj.product_type.available_count():
                raise ValidationError("Не допустимое число")

        #     products = products.objects.filter(product_type=obj, status="Ожидает заявку на отгрузку")[:amount]
        #     products.update(status="В процессе подтверждения", delivery=obj)
        #
        obj.seller = request.user.seller
        obj.save()

    def name(self, obj):
        return obj

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            form = deepcopy(WaitingDeliveryAdminForm)
            form.base_fields["amount"].label = f"Кол-во (доступно {obj.available_count()} шт)"
            return form
        else:
            return super().get_form(request, obj, **kwargs)


    name.short_description = "Название"


seller_panel.register(Product, ProductAdmin)
seller_panel.register(ProductType, ProductTypeAdmin)
seller_panel.register(Delivery, DeliveryAdmin)
