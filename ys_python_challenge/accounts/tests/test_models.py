from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class UserTest(TestCase):
    def test_create_user(self):
        username = "testuser"
        password = "test123"
        user = User.objects.create_user(
            username=username,
            password=password,
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
