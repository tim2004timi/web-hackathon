from django.db import models
from django.db.models import Q
from django.urls import reverse


class ProductType(models.Model):
    """
    Модель товара (продукта).
    ----------

    Атрибуты:
    article: AutoField
        Артикль товара - уникальный номер товара для его идентификации.
        Заполняется автоматически.

    name: CharField
        Наименование товара.

    size: CharField
        Размер товара в см (например 20*20*30).

    color: CharField
        Цвет товара.

    numbers: IntegerField
        Количество упаковок товара.
        По умолчанию стоит 1 шт.

    seller: ForeignKey
        Хозяин товара (продавец).
        Связь ManyToOne.

    status: CharField
        Статус товара.

    time_created: DateTimeField
        Поле для даты регистрации товара.
        Заполняется автоматически.
    """
    STATUSES = (
        ('В пути до нас', 'В пути до нас'),
        ('Ожидает заявку на отгрузку', 'Ожидает заявку на отгрузку'),
        ('В процессе подтверждения', 'В процессе подтверждения'),
        ('Ожидает штрихкод для тары', 'Ожидает штрихкод для тары'),
        ('Отгружено, ожидает оплаты', 'Отгружено, ожидает оплаты'),
        ('Оплата подтверждена', 'Оплата подтверждена'),
    )

    CIRCLE_COLORS_STYLES = {
        'В пути до нас': 'background: rgba(64, 117, 255, 0.4)',
        'Ожидает заявку на отгрузку': 'background: rgba(192, 47, 102, 0.6)',
        'В процессе подтверждения': 'background: rgba(239, 66, 132, 0.6)',
        'Ожидает штрихкод для тары': 'background: rgba(172, 65, 106, 0.6)',
        'Отгружено, ожидает оплаты': 'background: rgba(121, 121, 121, 0.6)',
        'Оплата подтверждена': '',
    }

    BUTTONS = {
        'В пути до нас': '',
        'Ожидает заявку на отгрузку': 'Добавить заявку',
        'В процессе подтверждения': '',
        'Ожидает штрихкод для тары': 'Добавить штрихкод',
        'Отгружено, ожидает оплаты': 'Ожидает оплаты',
        'Оплата подтверждена': '',
    }

    BUTTON_COLORS_STYLES = {
        'В пути до нас': 'color: #3063c9',
        'Ожидает заявку на отгрузку': 'color: #C02F66',
        'В процессе подтверждения': 'color: #EF4284',
        'Ожидает штрихкод для тары': 'color: #824F77',
        'Отгружено, ожидает оплаты': '',
        'Оплата подтверждена': '',
    }

    article = models.CharField(default=None,
                               max_length=30,
                               verbose_name="Артикул маркетплейса")
    name = models.CharField(default=None,
                            max_length=30,
                            verbose_name="Название")
    photo = models.ImageField(default=None,
                              blank=True,
                              null=True,
                              upload_to="uploads/photo",
                              verbose_name="Фото товара")
    size = models.CharField(default=None,
                            max_length=30,
                            verbose_name="Размер (20*20*30)")
    weight = models.IntegerField(default=1,
                                 verbose_name="Вес (кг)")
    seller = models.ForeignKey("Seller",
                               on_delete=models.CASCADE,
                               related_name="product_types",
                               verbose_name="Продавец")
    price = models.IntegerField(default=0,
                                verbose_name="Цена (руб)")

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def __str__(self):
        return self.name

    def available_count(self, product_type):
        return ProductType.objects.filter(product_type=product_type, products__status="Ожидает заявку на отгрузку").count()

    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = "Типы товаров"
