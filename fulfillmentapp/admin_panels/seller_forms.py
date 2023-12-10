from django.forms import ModelForm

from fulfillmentapp.models import Product, ProductType


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = ["seller", "delivery"]


class ProductTypeAdminForm(ModelForm):
    class Meta:
        model = ProductType
        exclude = ["seller"]


class DeliveryAdminForm(ModelForm):
    class Meta:
        model = ProductType
        exclude = ["seller"]


