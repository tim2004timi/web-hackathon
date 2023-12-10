from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User, Permission


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

    name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    email = models.EmailField(default=None, verbose_name="Почта")
    username = models.CharField(max_length=30, primary_key=True, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=30, verbose_name="Пароль")

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def save(self, *args, **kwargs):
        """Переопределение функции для добавления user со связью OneToOne"""
        if not self.user:
            user = User.objects.create(
                username=self.username,
                email=self.email,
                password=make_password(self.password),
                is_staff=True
            )
            self.add_permissions_to_user(user)
            self.user = user
        super().save(*args, **kwargs)

    @staticmethod
    def add_permissions_to_user(user: User):
        user.user_permissions.add(Permission.objects.get(codename="view_product"))
        user.user_permissions.add(Permission.objects.get(codename="change_product"))

        user.user_permissions.add(Permission.objects.get(codename="view_delivery"))
        user.user_permissions.add(Permission.objects.get(codename="change_delivery"))

        user.user_permissions.add(Permission.objects.get(codename="view_producttype"))
        user.user_permissions.add(Permission.objects.get(codename="change_producttype"))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы склада"
