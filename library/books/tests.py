from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Título del libro",
            subtitle = "Una pequeña descripción",
            author = "Yo mismo",
            isbn = "1234567890123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Título del libro")
        self.assertEqual(self.book.subtitle, "Una pequeña descripción")
        self.assertEqual(self.book.author, "Yo mismo")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pequeña")
        self.assertTemplateUsed(response, "books/book_list.html")