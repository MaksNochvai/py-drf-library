from django.urls import path

from .views import BorrowingViewSet, return_borrowing

app_name = "borrowings_service"

urlpatterns = [
    path(
        "",
        BorrowingViewSet.as_view({"get": "list", "post": "create"}),
        name="borrowing-list",
    ),
    path(
        "<pk>/", BorrowingViewSet.as_view({"get": "retrieve"}), name="borrowing-detail"
    ),
    path("<pk>/return/", return_borrowing, name="return-borrowing"),
]
