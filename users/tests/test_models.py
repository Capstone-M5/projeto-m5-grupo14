from django.test import TestCase
from users.models import User
from videos.models import Video


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

    def test_model_atribute_max_length(self):
        user = User.objects.get(username="ricardinho")
        name = user._meta.get_field("name").max_length
        username = user._meta.get_field("username").max_length
        email = user._meta.get_field("email").max_length

        self.assertEqual(name, 128)
        self.assertEqual(username, 128)
        self.assertTrue(username)
        self.assertEqual(email, 128)
        self.assertTrue(email)

    def test_model_atribute_unique(self):
        user = User.objects.get(username="ricardinho")
        username = user._meta.get_field("username").unique
        email = user._meta.get_field("email").unique

        self.assertTrue(username)
        self.assertTrue(email)

    def test_model_atribute_primary_key(self):
        user = User.objects.get(username="ricardinho")
        id = user._meta.get_field("id").primary_key
        self.assertTrue(id)

    def test_model_atributes_default(self):
        user = User.objects.get(username="ricardinho")
        is_superuser = user._meta.get_field("is_superuser").default
        is_active = user._meta.get_field("is_active").default
        self.assertFalse(is_superuser)
        self.assertTrue(is_active)
