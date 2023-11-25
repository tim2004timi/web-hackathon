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
    product = models.OneToOneField("Product",
                                   on_delete=models.CASCADE,
                                   primary_key=True,
                                   verbose_name="Товар")
    seller = models.ForeignKey("Seller",
                               on_delete=models.CASCADE,
                               related_name="deliveries",
                               verbose_name="Продавец")
    address = models.TextField(verbose_name="Адрес")
    driver_fio = models.CharField(max_length=50, verbose_name="ФИО водителя")
    car_number = models.CharField(max_length=20, verbose_name="Номер авто")
    date = models.DateField(verbose_name="Дата")
    barcode = models.ImageField(default=None, blank=True, verbose_name="Штрих-код")
    time_created = models.DateTimeField(auto_now_add=True)

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def __str__(self):
        return f"Отгрузка ({self.product.name})"

    class Meta:
        verbose_name = "Отгрузка"
        verbose_name_plural = "Отгрузки"
