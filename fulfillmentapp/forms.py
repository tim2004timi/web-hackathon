from django.forms import ModelForm

from fulfillmentapp.models import Delivery, Product


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
