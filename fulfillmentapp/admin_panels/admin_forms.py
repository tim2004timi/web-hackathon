from django.forms import ModelForm

from fulfillmentapp.models import Product, Seller, Operator, CallAssistant, ProductType


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


class SellerAdminForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ['user', "telegram_chat_id"]
        list_filter = ["status"]


class OperatorAdminForm(ModelForm):
    class Meta:
        model = Operator
        exclude = ['user']
        list_filter = ["status"]


class AssistantAdminForm(ModelForm):
    class Meta:
        model = CallAssistant
        exclude = ['telegram_chat_id']
