from rest_framework import serializers

import books_service.serializers
import users_service.serializers
from borrowings_service.models import Borrowing


class BorrowingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "user_id"
        )


class BorrowingDetailSerializer(serializers.ModelSerializer):
    book_id = books_service.serializers.BookSerializer(read_only=True)
    user_id = users_service.serializers.UserSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "user_id"
        )
