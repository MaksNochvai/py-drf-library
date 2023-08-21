from django.urls import path

from .views import PaymentViewSet

app_name = "payment_service"

urlpatterns = [
    path("", PaymentViewSet.as_view({"get": "list", "post": "create"}), name="payment-list"),
    path("<pk>/", PaymentViewSet.as_view({"get": "retrieve"}), name="payment-detail"),
    path("payment_success/", PaymentViewSet.as_view({"get": "payment_success"}), name="payment_success"),
    path("payment_cancel/", PaymentViewSet.as_view({"get": "payment_cancel"}), name="payment_cancel"),
]
