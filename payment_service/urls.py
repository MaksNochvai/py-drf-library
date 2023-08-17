from django.urls import path

from .views import PaymentViewSet

app_name = "payment_service"

urlpatterns = [
    path("", PaymentViewSet.as_view({"get": "list", "post": "create"}), name="payment-list"),
    path("<pk>/", PaymentViewSet.as_view({"get": "retrieve"}), name="payment-detail"),
]
