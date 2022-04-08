from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "test@email.com",
            password = "secret",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "El título",
            body = "Cuerpo del artículo",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "El título")
        self.assertEqual(self.post.body, "Cuerpo del artículo")
        self.assertEqual(str(self.post), "El título")
