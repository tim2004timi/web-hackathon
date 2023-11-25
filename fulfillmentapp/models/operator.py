from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User


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
