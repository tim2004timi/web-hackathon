from django.db import models
from django.urls import reverse


class Product(models.Model):
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
    article = models.AutoField(primary_key=True, verbose_name="Артикль")
    name = models.CharField(default=None, max_length=30, verbose_name="Название")
    size = models.CharField(default=None, max_length=30, verbose_name="Размер (20*20*30)")
    color = models.CharField(default=None, max_length=30, verbose_name="Цвет")
    numbers = models.IntegerField(default=1, verbose_name="Кол-во")
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE, related_name="products", verbose_name="Продавец")
    status = models.CharField(max_length=40, default="В пути до вас", blank=True, verbose_name="Статус")
    time_created = models.DateTimeField(auto_now_add=True)

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("product-slug", kwargs={"product_slug": f"product-{self.article}"})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
