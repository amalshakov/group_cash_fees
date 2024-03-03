from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Collect, Payment


# @receiver(post_save, sender=Collect)
# def send_email_on_creation_Collect(sender, instance, created, **kwargs):
#     if created:
#         author_email = instance.author.email
#         name_collect = instance.name
#         send_mail(
#             "Успех",
#             f"Вы успешно создали групповой денежный сбор - '{name_collect}'",
#             "am89681115653@yandex.ru",
#             [author_email],
#             fail_silently=False,
#         )


# @receiver(post_save, sender=Payment)
# def send_email_on_creation_Payment(sender, instance, created, **kwargs):
#     if created:
#         donating_email = instance.donating.email
#         name_collect = instance.collect.name
#         money = instance.money
#         send_mail(
#             "Успех",
#             f"Вы успешно внесли пожертвование в размере '{money}' на групповой денежный сбор - '{name_collect}'",
#             "am89681115653@yandex.ru",
#             [donating_email],
#             fail_silently=False,
#         )
