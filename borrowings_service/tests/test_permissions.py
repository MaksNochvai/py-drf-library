from django.test import TestCase
from datetime import date
from rest_framework.test import APIRequestFactory
from books_service.models import Book
from users_service.models import User
from borrowings_service.models import Borrowing
from borrowings_service.permissions import IsOwnerOrAdmin


class IsOwnerOrAdminPermissionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()

        cls.admin_user = User.objects.create_user(
            email="admin@example.com", password="adminpassword", is_staff=True
        )
        cls.normal_user = User.objects.create_user(
            email="user@example.com", password="userpassword"
        )

        cls.book = Book.objects.create(
            title="Test Book", author="Test Author", cover="HARD", inventory=10, daily_fee=1.99
        )
        cls.borrowing = Borrowing.objects.create(
            borrow_date=date(2023, 1, 1),
            expected_return_date=date(2023, 1, 10),
            actual_return_date=None,
            book_id=cls.book,
            user_id=cls.normal_user,
        )

    def test_admin_has_permission(self):
        request = self.factory.get("/api/borrowings/")
        request.user = self.admin_user
        permission = IsOwnerOrAdmin()
        has_permission = permission.has_object_permission(request, None, self.borrowing)
        self.assertTrue(has_permission)

    def test_user_is_owner_and_no_actual_return(self):
        request = self.factory.get("/api/borrowings/")
        request.user = self.normal_user
        permission = IsOwnerOrAdmin()
        has_permission = permission.has_object_permission(request, None, self.borrowing)
        self.assertTrue(has_permission)

    def test_user_is_not_owner(self):
        another_user = User.objects.create_user(
            email="anotheruser@example.com", password="anotherpassword"
        )
        request = self.factory.get("/api/borrowings/")
        request.user = another_user
        permission = IsOwnerOrAdmin()
        has_permission = permission.has_object_permission(request, None, self.borrowing)
        self.assertFalse(has_permission)

    def test_user_is_owner_but_has_actual_return(self):
        self.borrowing.actual_return_date = date(2023, 1, 5)
        self.borrowing.save()
        request = self.factory.get("/api/borrowings/")
        request.user = self.normal_user
        permission = IsOwnerOrAdmin()
        has_permission = permission.has_object_permission(request, None, self.borrowing)
        self.assertFalse(has_permission)
