from collects.models import Collect, Payment
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, Count
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """."""

    class Meta:
        model = User
        fields = ("id",)


class PaymentSerializer(serializers.ModelSerializer):
    """."""

    payer_name = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = (
            "id",
            "money",
            "date_time_payment",
            "payer_name",
        )

    def get_payer_name(self, obj):
        return obj.donating.get_full_name()


class CollectSerializer(serializers.ModelSerializer):
    """."""

    author_name = serializers.SerializerMethodField()
    occasion = serializers.CharField(source="get_occasion_display")
    current_money = serializers.SerializerMethodField()
    current_people = serializers.SerializerMethodField()
    payments = PaymentSerializer(many=True)

    class Meta:
        model = Collect
        fields = (
            "id",
            "author_name",
            "name",
            "occasion",
            "description",
            "purpose",
            "logo",
            "date_time_collect",
            "current_money",
            "current_people",
            "payments",
        )

    def get_author_name(self, obj):
        return obj.author.get_full_name()

    def get_current_money(self, obj):
        return obj.payments.aggregate(Sum("money"))["money__sum"]

    def get_current_people(self, obj):
        return obj.payments.all().values("donating_id").distinct().count()
