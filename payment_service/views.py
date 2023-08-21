import stripe
from django.urls import reverse
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Payment
from .permissions import IsOwnerOrAdmin
from .serializers import PaymentListSerializer, PaymentDetailSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [IsOwnerOrAdmin()]
        elif self.action == "create":
            return [IsAuthenticated()]

        return [IsAuthenticated(), IsOwnerOrAdmin()]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PaymentDetailSerializer

        return PaymentListSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "borrowing_id",
                type=OpenApiTypes.INT,
                description="Filter by borrowing id",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Authentication credentials were not provided.")

        queryset = self.queryset

        if not request.user.is_staff:
            queryset = queryset.filter(borrowing_id__user_id=request.user)

        borrowing_id = self.request.query_params.get("borrowing_id")
        if borrowing_id:
            queryset = queryset.filter(borrowing_id=int(borrowing_id))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def create_payment_session(self, request, pk=None):
        payment = self.get_object()
        success_url = reverse("payment_success")
        cancel_url = reverse("payment_cancel")

        session = stripe.checkout.Session.create(
            success_url=success_url,
            cancel_url=cancel_url,
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(payment.money_to_pay * 100),
                        "product_data": {
                            "name": "Payment for borrowing",
                        },
                    },
                    "quantity": 1,
                },
            ],
        )

        payment.session_id = session.id
        payment.session_url = session.url
        payment.save()

        return Response({"session_id": session.id, "session_url": session.url})

    @action(detail=False, methods=["get"])
    def payment_success(self, request):
        return Response({"message": "Payment successful"})

    @action(detail=False, methods=["get"])
    def payment_cancel(self, request):
        return Response({"message": "Payment cancelled"})
