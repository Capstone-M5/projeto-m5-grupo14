from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "ricardinho",
            "name": "Ricardo Souza",
            "password": "Ricardo10",
            "email": "ricardo@outlook.com",
        }

        cls.user = User.objects.create_user(**cls.user_data)

    def test_model_atribute(self):
        user = User.objects.get(username="ricardinho")
        name = user._meta.get_field("name").max_length
        username = user._meta.get_field("username").max_length
        email = user._meta.get_field("email").max_length

        self.assertEqual(name, 128)
        self.assertEqual(username, 128)
        self.assertEqual(email, 128)
        self.assertEqual(self.user.name, user.name)
        self.assertEqual(self.user.username, user.username)
        self.assertEqual(self.user.email, user.email)
        self.assertEqual(self.user.password, user.password)
