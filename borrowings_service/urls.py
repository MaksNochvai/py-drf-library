from django.urls import path

from borrowings_service.views import BorrowingViewSet

app_name = "borrowings_service"

urlpatterns = [
    path("", BorrowingViewSet.as_view({"get": "list", "post": "create"}), name="borrowing-list"),
    path("<pk>/", BorrowingViewSet.as_view(
        {"get": "retrieve", "put": "update", "delete": "destroy"}),
         name="borrowing-detail"
         ),
]