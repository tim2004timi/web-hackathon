from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User, Permission


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
        Поле для username telegram продавца (заказчика).
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
                password=make_password(self.password),
                is_staff=True
            )
            self.add_permissions_to_user(user)
            self.user = user
        super().save(*args, **kwargs)

    @staticmethod
    def add_permissions_to_user(user: User):
        user.user_permissions.add(Permission.objects.get(codename="add_product"))
        user.user_permissions.add(Permission.objects.get(codename="view_product"))
        user.user_permissions.add(Permission.objects.get(codename="change_product"))

        user.user_permissions.add(Permission.objects.get(codename="add_delivery"))
        user.user_permissions.add(Permission.objects.get(codename="view_delivery"))
        user.user_permissions.add(Permission.objects.get(codename="change_delivery"))

        user.user_permissions.add(Permission.objects.get(codename="add_producttype"))
        user.user_permissions.add(Permission.objects.get(codename="view_producttype"))
        user.user_permissions.add(Permission.objects.get(codename="change_producttype"))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"
