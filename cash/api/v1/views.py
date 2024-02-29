from collects.models import Collect, Payment
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets

from .serializers import CollectSerializer, PaymentSerializer, UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CollectViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
