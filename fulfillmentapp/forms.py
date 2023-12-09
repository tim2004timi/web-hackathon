from django.forms import ModelForm

from fulfillmentapp.models import Delivery, Product, Seller, Operator


class DeliveryAdminForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ["seller"]

    def __init__(self, *args, **kwargs):
        super(DeliveryAdminForm, self).__init__(*args, **kwargs)
        # Ограничиваем выбор Product только незанятыми объектами
        try:
            self.fields['product'].queryset = Product.objects.filter(delivery__isnull=True)
        except Exception as e:
            print(e)


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
        exclude = ["seller"]


class DeliveryAdminForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ["seller"]

    def __init__(self, *args, **kwargs):
        super(DeliveryAdminForm, self).__init__(*args, **kwargs)
        # Ограничиваем выбор Product только незанятыми объектами
        try:
            self.fields['product'].queryset = Product.objects.filter(delivery__isnull=True)
        except Exception as e:
            print(e)

    def save_model(self, request, obj, form, change):
        obj.seller = request.user.seller
        super().save_model(request, obj, form, change)


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
        model = Operator
        exclude = ['telegram_chat_id']

