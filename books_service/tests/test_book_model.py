import pytest
from django.test import TestCase
from books_service.models import Book, CoverType


@pytest.mark.django_db
class TestBookModel(TestCase):
    def setUp(self):
        self.book_data = {
            "title": "Sample Book",
            "author": "John Doe",
            "cover": CoverType.HARD.value,
            "inventory": 10,
            "daily_fee": 1.99,
        }

    def test_create_book(self):
        book = Book.objects.create(**self.book_data)
        self.assertEqual(Book.objects.count(), 1)

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        new_title = "Updated Book Title"
        book.title = new_title
        book.save()
        updated_book = Book.objects.get(pk=book.pk)
        self.assertEqual(updated_book.title, new_title)

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        book.delete()
        self.assertEqual(Book.objects.count(), 0)

    def test_get_cover_type_display(self):
        book = Book.objects.create(**self.book_data)
        self.assertEqual(book.get_cover_display(), "HARD")
