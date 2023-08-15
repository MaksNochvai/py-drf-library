from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from borrowings_service.models import Borrowing
from borrowings_service.serializers import BorrowingSerializer


class BorrowingViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
