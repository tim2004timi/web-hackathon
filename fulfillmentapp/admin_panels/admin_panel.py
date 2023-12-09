from typing import Any

from django.contrib import admin
from django.utils.html import format_html
from django.forms import ModelForm

from ..models import Product

class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = []

class AdminPanel(admin.AdminSite):
    form = ProductAdminForm
    list_display = ("name", "article", "color", "numbers", "seller", "colored_status", "delivery")
    search_fields = ["article", "name", "size", "color", "numbers", "status"]
    list_filter = ["status"]

    def colored_status(self, obj):
        # Замените 'В пути до нас' на тот статус, который вам нужно выделить красным
        return format_html('<span style="{}">{}</span>', obj.get_button_style(), obj.status)

    colored_status.short_description = 'Статус'
    
admin_panel = AdminPanel(name='admin_panel')

admin_panel.register(Product, AdminPanel)