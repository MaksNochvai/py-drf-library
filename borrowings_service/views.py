from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Borrowing
from .serializers import BorrowingListSerializer, BorrowingDetailSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BorrowingDetailSerializer

        return BorrowingListSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "book_id",
                type=OpenApiTypes.INT,
                description="Filter by book id",
            ),
            OpenApiParameter(
                "user_id",
                type=OpenApiTypes.INT,
                description="Filter by user id",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        queryset = self.queryset

        book_id = self.request.query_params.get("book_id")
        if book_id:
            queryset = queryset.filter(book_id=int(book_id))

        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user_id=int(user_id))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
