from copy import deepcopy

from django.forms import ModelForm
from django import forms

from fulfillmentapp.models import Product, ProductType, Delivery


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = ["seller", "delivery"]


class ProductTypeAdminForm(ModelForm):
    class Meta:
        model = ProductType
        exclude = ["seller"]


class WaitingDeliveryAdminForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ["label", "marketplace_barcode"]

    amount = forms.IntegerField(label="Кол-во")

    # def __init__(self, *args, **kwargs):
    #     form = deepcopy(WaitingDeliveryAdminForm)
    #     form.amount.label = f"Кол-во (доступно {} шт)"
    #     super(WaitingDeliveryAdminForm, self).__init__(*args, **kwargs)



