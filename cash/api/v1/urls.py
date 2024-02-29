from django.urls import include, path
from rest_framework import routers

from .views import CollectViewSet, PaymentViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r"users", UserViewSet, basename="users")
router.register(r"payments", PaymentViewSet, basename="payments")
router.register(r"collects", CollectViewSet, basename="collects")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
