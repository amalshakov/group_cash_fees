import json
import os

from django.conf import settings
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
        data = process_file("users.json")
        for email, value in data.items():
            User.objects.create(
                email=email,
                password=value[0],
                first_name=value[1],
                last_name=value[2],
                username=value[3],
            )
        print("-----Пользователи загружены!-----")
