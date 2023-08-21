from django.test import TestCase
from django.urls import reverse

from books_service.models import Book
from users_service.models import User
from .models import Payment, PaymentStatus, PaymentType
from borrowings_service.models import Borrowing


class PaymentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(email="user@example.com", password="password")
        cls.book = Book.objects.create(title="Sample Book", author="John Doe", cover="HARD", inventory=5,
                                       daily_fee=1.99)
        cls.borrowing = Borrowing.objects.create(
            borrow_date="2023-08-01", expected_return_date="2023-08-15", book_id=cls.book, user_id=cls.user
        )
        cls.payment = Payment.objects.create(
            status=PaymentStatus.PENDING.value,
            type=PaymentType.PAYMENT.value,
            borrowing_id=cls.borrowing,
            session_url="http://example.com/session/",
            session_id="session123",
            money_to_pay=10.99,
        )

    def test_status_display(self):
        self.assertEqual(self.payment.get_status_display(), PaymentStatus.PENDING.name)

    def test_type_display(self):
        self.assertEqual(self.payment.get_type_display(), PaymentType.PAYMENT.name)

    def test_str_representation(self):
        expected_str = f"Payment #{self.payment.id} - {PaymentStatus.PENDING.value} - {PaymentType.PAYMENT.value}"
        self.assertEqual(str(self.payment), expected_str)

    def test_session_url_blank_and_null(self):
        payment = Payment.objects.create(
            status=PaymentStatus.PENDING.value,
            type=PaymentType.PAYMENT.value,
            borrowing_id=self.borrowing,
            money_to_pay=10.00
        )

        self.assertTrue(payment.session_url in (None, ''))

    def test_session_id_blank_and_null(self):
        payment = Payment.objects.create(
            status=PaymentStatus.PENDING.value,
            type=PaymentType.PAYMENT.value,
            borrowing_id=self.borrowing,
            money_to_pay=10.00
        )

        self.assertTrue(payment.session_id in (None, ''))
