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
            "book_id",
            "user_id"
        )

    def create(self, validated_data):
        book = validated_data["book_id"]
        borrowing = Borrowing.objects.create(
            book_id=book,
            borrow_date=validated_data["borrow_date"],
            expected_return_date=validated_data["expected_return_date"],
            user_id=self.context["request"].user,
        )
        book.inventory -= 1
        book.save()
        return borrowing


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
