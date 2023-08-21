from django.test import TestCase
from datetime import date
from books_service.models import Book
from users_service.models import User
from borrowings_service.models import Borrowing


class BorrowingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email="testuser@gmail.com", password="testpassword"
        )
        cls.book = Book.objects.create(
            title="Test Book", author="Test Author", cover="HARD", inventory=10, daily_fee=1.99
        )
        cls.borrowing = Borrowing.objects.create(
            borrow_date=date(2023, 1, 1),
            expected_return_date=date(2023, 1, 10),
            actual_return_date=None,
            book_id=cls.book,
            user_id=cls.user,
        )

    def test_borrowing_str(self):
        expected_str = f"Borrowing of {self.book} by {self.user}"
        self.assertEqual(str(self.borrowing), expected_str)

    def test_borrowing_with_actual_return_date(self):
        self.borrowing.actual_return_date = date(2023, 1, 5)
        self.borrowing.save()
        self.assertEqual(self.borrowing.actual_return_date, date(2023, 1, 5))
