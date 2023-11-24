from django.contrib.auth.hashers import make_password
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="seller")
    name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    username = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    email = models.EmailField(blank=True, default=None, verbose_name="Почта")
    telegram = models.CharField(max_length=30, blank=True, default=None, verbose_name="Телеграм")
    telegram_chat_id = models.CharField(default="", blank=True)
    time_signup = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="operator")
    username = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")

    objects = models.Manager()

    def save(self, *args, **kwargs):
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
    article = models.AutoField(primary_key=True, verbose_name="Артикль")
    name = models.CharField(default=None, max_length=30, verbose_name="Название")
    size = models.CharField(default=None, max_length=30, verbose_name="Размер (20х20х30)")
    color = models.CharField(default=None, max_length=30, verbose_name="Цвет")
    numbers = models.IntegerField(default=1, verbose_name="Кол-во")
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE, verbose_name="Продавец")
    status = models.CharField(max_length=20, default=None, blank=True, verbose_name="Статус")

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Delivery(models.Model):
    product = models.OneToOneField("Product", on_delete=models.CASCADE, primary_key=True, verbose_name="Товар")
    address = models.TextField(verbose_name="Адрес")
    driver_fio = models.CharField(max_length=50, verbose_name="ФИО водителя")
    car_number = models.CharField(max_length=20, verbose_name="Номер авто")
    date = models.DateField(verbose_name="Дата")
    qr = models.ImageField(verbose_name="QR")

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
