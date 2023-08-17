from rest_framework import serializers

import books_service.serializers
import borrowings_service.serializers
import users_service.serializers
from borrowings_service.models import Borrowing


class PaymentListSerializer(serializers.ModelSerializer):
    actual_return_date = serializers.ReadOnlyField()

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "status",
            "type",
            "borrowing_id",
            "session_url",
            "session_id",
            "money_to_pay",
        )


class PaymentDetailSerializer(serializers.ModelSerializer):
    borrowing_id = borrowings_service.serializers.BorrowingListSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "status",
            "type",
            "borrowing_id",
            "session_url",
            "session_id",
            "money_to_pay",
        )

