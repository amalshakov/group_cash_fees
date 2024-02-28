from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Payment(models.Model):
    """Модель описывающая Платеж для сбора."""

    money = models.PositiveIntegerField(
        verbose_name="Сумма пожертвования",
        help_text="Введите сумму пожертвования",
    )
    date_time_payment = models.DateTimeField(
        verbose_name="Дата и время платежа"
    )
    donating = models.ForeignKey(User, on_delete=models.PROTECT)


class Collect(models.Model):
    """Модель Группового денежного сбора."""

    OCCASION_TYPES = (
        ("birthday", "День рождение"),
        ("wedding", "Свадьба"),
        ("new_year", "Новый год"),
    )
    occasion = models.CharField(
        choices=OCCASION_TYPES,
        max_length=50,
        verbose_name="Повод для сбора",
        help_text="Введите повод для сбора",
    )
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(
        max_length=50,
        verbose_name="Название сбора",
        help_text="Введите название сбора",
    )
    description = models.TextField(
        verbose_name="Описание сбора", help_text="Введите описание сбора"
    )
    purpose = models.PositiveIntegerField(
        verbose_name="Сумма, которую запланировали собрать",
        help_text="Введите сумму, которую планируете собрать",
    )
    current_money = models.PositiveIntegerField(
        verbose_name="Сумма, которую собрали на текущий момент"
    )
    count_people = models.PositiveIntegerField(
        verbose_name="Количество людей, уже сделавших пожертвования"
    )
    logo = models.ImageField(
        verbose_name="Обложка сбора",
        help_text="Загрузите картинку",
        upload_to="collects/images/logo",
        null=True,
    )
    date_time_collect = models.DateTimeField(
        verbose_name="Дата и время завершения сбора",
        help_text="Введите дату и время завершения сбора",
    )
