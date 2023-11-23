from django.contrib import admin
from django.forms import ModelForm

from .models import Product, Delivery, Operator, Seller


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("article", "name", "size", "color", "numbers", "seller", "status", "delivery")
    search_fields = ["article", "name", "size", "color", "numbers", "status"]


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("product", "address", "date", "driver_fio", "qr")
    search_fields = ["product", "address", "date", "driver_fio"]


class SellerAdminForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ['user']


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


admin.site.register(Operator, OperatorAdmin)
admin.site.register(Seller, SellerAdmin)
