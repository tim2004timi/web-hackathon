from django.forms import ModelForm, Form
from django import forms

from fulfillmentapp.models import Product, ProductType


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = ["delivery"]


class ProductTypeAdminForm(ModelForm):
    class Meta:
        model = Product
        fields = []

    amount = forms.IntegerField(label="Кол-во")


class DeliveryAdminForm(ModelForm):
    class Meta:
        model = ProductType
        exclude = []

    # def __init__(self, *args, **kwargs):
    #     super(DeliveryAdminForm, self).__init__(*args, **kwargs)
    #     # Ограничиваем выбор Product только незанятыми объектами
    #     product_types = forms.ChoiceField(choices=[
    #     ('значение1', 'Отображаемое значение 1'),
    #     ('значение2', 'Отображаемое значение 2'),
    #     ('значение3', 'Отображаемое значение 3'),
    #     # Добавьте свои варианты значений и отображаемых названий
    # ], widget=forms.Select(attrs={'class': 'ваш_класс_стиля'}))


