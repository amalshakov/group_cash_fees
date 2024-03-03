import json
import os

from collects.models import Collect, Payment
from django.conf import settings
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


def process_file(name: str):
    with open(
        os.path.join(settings.BASE_DIR, "data/", name),
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = process_file("payments.json")
        for name, value in data.items():
            Payment.objects.get_or_create(
                money=value[0],
                donating=User.objects.get(id=value[1]),
                collect=Collect.objects.get(id=value[2]),
            )
        print("-----Платежи загружены!-----")
