from django.utils import timezone
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Borrowing
from .permissions import IsOwnerOrAdmin
from .serializers import BorrowingListSerializer, BorrowingDetailSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingListSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [IsOwnerOrAdmin()]
        elif self.action == "create":
            return [IsAuthenticated()]

        return [IsAuthenticated(), IsOwnerOrAdmin()]

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
            OpenApiParameter(
                "is_active",
                type=OpenApiTypes.BOOL,
                description="Filter by active borrowings",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Authentication credentials were not provided.")

        queryset = self.queryset

        if not request.user.is_staff:
            queryset = queryset.filter(user_id=request.user)

        book_id = self.request.query_params.get("book_id")
        if book_id:
            queryset = queryset.filter(book_id=int(book_id))

        user_id = self.request.query_params.get("user_id")
        if user_id and request.user.is_staff:
            queryset = queryset.filter(user_id=int(user_id))

        is_active = self.request.query_params.get("is_active")
        if is_active:
            if is_active.lower() == "true":
                queryset = queryset.filter(actual_return_date__isnull=True)
            elif is_active.lower() == "false":
                queryset = queryset.filter(actual_return_date__isnull=False)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def return_borrowing(request, pk):
    try:
        borrowing = Borrowing.objects.get(pk=pk)
    except Borrowing.DoesNotExist:
        return Response(
            {"detail": "Borrowing not found."}, status=status.HTTP_404_NOT_FOUND
        )

    if borrowing.actual_return_date:
        return Response(
            {"detail": "This borrowing has already been returned."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    borrowing.actual_return_date = timezone.now()
    borrowing.save()

    book = borrowing.book_id
    book.inventory += 1
    book.save()

    return Response(
        {"detail": "Borrowing has been successfully returned."},
        status=status.HTTP_200_OK,
    )
