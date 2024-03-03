from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User = get_user_model()


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
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="collects",
        verbose_name="Автор сбора",
    )
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
        validators=(
            MinValueValidator(1, "Нужно постараться собрать хоть, что-то"),
        ),
    )
    # current_money = models.PositiveIntegerField(
    #     verbose_name="Сумма, которую собрали на текущий момент",
    #     default=0,
    #     editable=False,
    # )
    # count_people = models.PositiveIntegerField(
    #     verbose_name="Количество людей, уже сделавших пожертвования",
    #     editable=False,
    #     default=0,
    # )
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

    class Meta:
        verbose_name = "Групповой денежный сбор"
        verbose_name_plural = "Групповые денежные сборы"

    def __str__(self) -> str:
        return self.name


class Payment(models.Model):
    """Модель описывающая Платеж для сбора."""

    money = models.PositiveIntegerField(
        verbose_name="Сумма пожертвования",
        help_text="Введите сумму пожертвования",
        validators=(MinValueValidator(1, "Пожертвуйте хоть что-нибудь"),),
    )
    date_time_payment = models.DateTimeField(
        verbose_name="Дата и время платежа", auto_now_add=True
    )
    donating = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="payments",
        verbose_name="Пользователь, делающий пожертвование",
    )
    collect = models.ForeignKey(
        Collect,
        on_delete=models.PROTECT,
        related_name="payments",
        verbose_name="Групповой денежный сбор",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
