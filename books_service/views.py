from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from books_service.models import Book
from books_service.permissions import IsAdminOrIfAuthenticatedReadOnly
from books_service.serializers import BookSerializer


class BookViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
