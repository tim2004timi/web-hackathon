from django.contrib.auth.hashers import make_password
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Seller(models.Model):
    """
    Модель продавца (заказчика).
    ----------

    Атрибуты:
    user: OneToOneField
        Связь один к одному с User из django.contrib.auth.models.User.
        Поле для для авторизации и аутентификации пользователя в системе через встроенные возможности user.
        Заполняется автоматически переопределенной функцией save().

    name: CharField
        Поле для имени продавца (заказчика).

    last_name: CharField
        Поле для фамилии продавца (заказчика).

    username: CharField
        Поле для логина продавца (заказчика).

    password: CharField
        Поле для пароля продавца (заказчика).

    email: EmailField
        Поле для почты продавца (заказчика).

    telegram: CharField
        Поле для логина продавца (заказчика).
        Пригодиться для интерфейса через мессенджер telegram.
        Через telegram отправляются новые уведомления пользователям о новых изменениях.

    telegram_chat_id: CharField
        Поле для ID чата в telegram продавца (заказчика).
        Оно пустое по дефолту, но при первом сообщение пользователя оно заполняется.

    time_signup: models.DateTimeField
        Поле для даты регистрации продавца (заказчика).
        Заполняется автоматически.
    """
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                related_name="seller")

    name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    username = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    email = models.EmailField(blank=True, default=None, verbose_name="Почта")
    telegram = models.CharField(max_length=30, blank=True, default=None, verbose_name="Телеграм")
    telegram_chat_id = models.CharField(default="", blank=True)
    time_signup = models.DateTimeField(auto_now_add=True)

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def save(self, *args, **kwargs):
        """Переопределение функции для добавления user со связью OneToOne"""
        if not self.user:
            user = User.objects.create(
                username=self.username,
                email=self.email,
                password=make_password(self.password)
            )
            self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"


class Operator(models.Model):
    """
    Модель оператора склада.
    Его задачи:
        Подтверждать прибытие товаров на склад.
        Заполнять некоторые поля у товаров.
        Вести отчет и аналитику о товарах.
    ----------

    Атрибуты:
    user: OneToOneField
        Связь один к одному с User из django.contrib.auth.models.User.
        Поле для для авторизации и аутентификации пользователя в системе через встроенные возможности user.
        Заполняется автоматически переопределенной функцией save().

    username: CharField
        Поле для логина оператора склада.

    password: CharField
        Поле для пароля оператора склада.
    """
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                related_name="operator")

    username = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def save(self, *args, **kwargs):
        """Переопределение функции для добавления user со связью OneToOne"""
        if not self.user:
            user = User.objects.create(
                username=self.username,
                email=self.username,
                password=make_password(self.password)
            )
            self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы"


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
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE, verbose_name="Продавец")
    status = models.CharField(max_length=20, default=None, blank=True, verbose_name="Статус")
    time_created = models.DateTimeField(auto_now_add=True)

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Delivery(models.Model):
    """
    Модель поставки.
    В нее входят данные о товаре, дате, адресе, ФИО водителя, номер авто и штрих-коде.
    ----------

    Атрибуты:
    product: OneToOneField
        Связь OneToOne с товаром для которого осуществляется поставка.

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


class CallAssistant(models.Model):
    telegram = models.CharField(max_length=30, blank=True, default=None, verbose_name="Телеграм")
    telegram_chat_id = models.CharField(default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.telegram}"

    class Meta:
        verbose_name = "Ассистент"
        verbose_name_plural = "Ассистенты"
