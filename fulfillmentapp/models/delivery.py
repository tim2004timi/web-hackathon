from django.db import models


class Delivery(models.Model):
    """
    Модель отгрузки.
    В нее входят данные о товаре, дате, адресе, ФИО водителя, номер авто и штрих-коде.
    ----------

    Атрибуты:
    product: OneToOneField
        Связь OneToOne с товаром для которого осуществляется поставка.

    seller: ForeignKey
        Хозяин товара (продавец).
        Связь ManyToOne.

    address: TextField
        Поле для адреса доставки.

    driver_fio: CharField
        ФИО водителя.

    car_number: CharField
        Номер автомобиля водителя.

    date: DateField
        Дата отгрузки.

    barcode: ImageField
        Штрих-код от маркетплейса.

    time_created: DateTimeField
        Поле для даты регистрации товара.
        Заполняется автоматически.
    """

    address = models.TextField(blank=True, null=True, verbose_name="Адрес")
    driver_fio = models.CharField(blank=True, null=True, max_length=50, verbose_name="ФИО водителя")
    car_number = models.CharField(blank=True, null=True, max_length=20, verbose_name="Номер авто")
    date = models.DateField(blank=True, null=True, verbose_name="Дата")
    time_created = models.DateTimeField(auto_now_add=True)
    label = models.FileField(default=None,
                             upload_to="labels/",
                             null=True,
                             blank=True,
                             editable=True,
                             verbose_name="Этикетка")
    marketplace_barcode = models.FileField(null=True,
                                           upload_to="marketplace_barcodes/",
                                           editable=True,
                                           verbose_name="Штрих-код для маркетплейса")
    wrapper_barcode = models.FileField(default=None,
                                       upload_to="wrapper_barcodes/",
                                       null=True,
                                       blank=True,
                                       editable=True,
                                       verbose_name="Штрих-код для тары")
    bill = models.FileField(default=None,
                            upload_to="bills/",
                            null=True,
                            blank=True,
                            editable=True,
                            verbose_name="Счет")
    seller = models.ForeignKey("Seller",
                               on_delete=models.CASCADE,
                               null=True,
                               default=None,
                               related_name="deliveries",
                               verbose_name="Продавец")
    product_type = models.ForeignKey("ProductType",
                                     on_delete=models.CASCADE,
                                     related_name="deliveries",
                                     verbose_name="Тип товара")

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def save(self, *args, **kwargs):
        """Переопределение функции для добавления seller"""
        if not self.seller:
            self.seller = self.products.first().seller
        super().save(*args, **kwargs)

    def available_count(self):
        return self.product_type.available_count()

    def __str__(self):
        return f"Отгрузка ({self.product_type})"

    class Meta:
        verbose_name = "Отгрузка"
        verbose_name_plural = "Отгрузки"
