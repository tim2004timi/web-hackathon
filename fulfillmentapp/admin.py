from django.contrib import admin
from .models import Seller, Product, Delivery, Operator


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "login", "password", "email", "telegram", "time_signup")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("article", "name", "size", "color", "numbers", "seller", "status", "delivery")


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("product", "address", "date", "driver_fio", "qr")


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ("login", "password")
