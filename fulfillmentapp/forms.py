from django.forms import ModelForm

from fulfillmentapp.models import Delivery, Product, Seller, Operator, ProductType, CallAssistant


class DeliveryAdminForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = []

    # def __init__(self, *args, **kwargs):
    #     super(DeliveryAdminForm, self).__init__(*args, **kwargs)
    #     # Ограничиваем выбор Product только незанятыми объектами
    #     try:
    #         self.fields['product'].queryset = Product.objects.filter(delivery__isnull=True)
    #     except Exception as e:
    #         print(e)


class AdminWaitingDeliveryForm(DeliveryAdminForm):
    class Meta:
        model = Delivery
        exclude = ["seller", "bill", "wrapper_barcode", "address", "driver_fio", "car_number", "date"]


class AdminWaitingConfirmForm(DeliveryAdminForm):
    class Meta:
        model = Delivery
        exclude = ["product", "seller", "label", "marketplace_barcode", "wrapper_barcode", "bill"]


class AdminWaitingWrapperBarcodeForm(DeliveryAdminForm):
    class Meta:
        model = Delivery
        exclude = ["product", "seller", "label", "marketplace_barcode", "bill", "address", "driver_fio", "car_number", "date"]


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = []


class ProductTypeAdminForm(ModelForm):
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

