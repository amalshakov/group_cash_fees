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
        data = process_file("collects.json")
        for name, value in data.items():
            collect, created = Collect.objects.get_or_create(
                occasion=value[0],
                name=name,
                description=value[1],
                purpose=value[2],
                date_time_collect=value[3],
                author=User.objects.get(id=value[4]),
            )
            with open(f"data/db_image/{name}.jpg", "rb") as file:
                image = ImageFile(file)
                collect.logo.save(f"{name}.jpg", image)
        print("-----Групповые сборы загружены!-----")
