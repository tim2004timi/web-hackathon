from django.db import models


class CallAssistant(models.Model):
    """
    Модель ассистента по заявкам на регистрации.
    Ассистентам приходят сообщения в telegram с данными заявок на регистрацию продавцов (заказчиков).
    ----------

    Атрибуты:
    telegram: CharField
        Поле для username telegram ассистента.
        Пригодиться для интерфейса через мессенджер telegram.
        Через telegram отправляются новые заявки на регистрацию.

    telegram_chat_id: CharField
        Поле для ID чата в telegram ассистента.
        Оно пустое по дефолту, но при первом сообщение пользователя оно заполняется.
    """
    telegram = models.CharField(max_length=30, blank=True, default=None, verbose_name="Телеграм")
    telegram_chat_id = models.CharField(default="", blank=True)

    # Объявление дефолтного manager для ORM
    objects = models.Manager()

    def __str__(self):
        return f"{self.telegram}"

    class Meta:
        verbose_name = "Ассистент"
        verbose_name_plural = "Ассистенты"
