from rest_framework import status, viewsets
from collects.models import Payment, Collect
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """."""

    queryset = User.objects.all()
    serializer_class = 


class PaymentViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Payment.objects.all()
    serializer_class = 

class CollectViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Collect.objects.all()
    serializer_class = 
