from rest_framework import serializers

import borrowings_service.serializers
from payment_service.models import PaymentStatus, PaymentType, Payment


class PaymentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            "id",
            "status",
            "type",
            "borrowing_id",
            "money_to_pay",
        )


class PaymentDetailSerializer(serializers.ModelSerializer):
    borrowing_id = borrowings_service.serializers.BorrowingListSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = (
            "id",
            "status",
            "type",
            "borrowing_id",
            "money_to_pay",
        )
