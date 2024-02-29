from collects.models import Collect, Payment
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = User
        fields = ("id",)


class PaymentSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = Payment
        fields = ("id",)


class CollectSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = Collect
        fields = ("id",)
