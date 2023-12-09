from django.forms import ModelForm

from fulfillmentapp.models import Product, ProductType


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = []


class ProductTypeAdminForm(ModelForm):
    class Meta:
        model = ProductType
        exclude = []


class DeliveryAdminForm(ModelForm):
    class Meta:
        model = ProductType
        exclude = []


