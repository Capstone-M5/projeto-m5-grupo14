from django.test import TestCase
from users.models import User
from videos.models import Video
from reviews.models import Review


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "ricardinho",
            "name": "Ricardo Souza",
            "password": "Ricardo10",
            "email": "ricardo@outlook.com",
        }

        cls.video_data_1 = {
            "title": "Video Legal",
            "thumbnail": "ajsdhkajsdhkajsdhgfdrs",
            "link": "http://youtube.com/adasdadasd",
            "downloads": 1
        }

        cls.video_data_2 = {
            "title": "Video de gatinhos",
            "thumbnail": "ajsdhkasklkslksaksksçafdrs",
            "link": "http://youtube.com/aaoksjjsjdjdjfh",
            "downloads": 1
        }

        cls.data_users = {
            "name": "ronaldo",
            "password": "Ronaldo10",
        }

        cls.review_data = {
            "text": "Vídeo ótimo!",
            "rating": 10
        }

        cls.user = User.objects.create_user(**cls.user_data)

        cls.video = Video.objects.create(**cls.video_data_1)

        cls.users = [User.objects.create_user(
            **cls.data_users, username=f'aleatório{i}', email=f'{i}aleatorio@email.com') for i in range(10)]

        cls.reviews = [Review.objects.create(
            **cls.review_data, video=cls.video, user=cls.user) for _ in range(5)]

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

    def test_user_fields(self):
        self.assertEqual(self.user.username, self.user_data["username"])
        self.assertEqual(self.user.name, self.user_data["name"])
        self.assertEqual(self.user.email, self.user_data["email"])

    def test_multiple_users_can_be_attached_to_one_video(self):
        for user in self.users:
            self.video.users.add(user)

        self.assertEquals(len(self.users), self.video.users.count())

        for user in self.users:
            self.assertIn(self.video, user.videos.all())

    def test_can_user_write_multiple_reviews(self):
        for review in self.reviews:
            self.assertIs(review.user, self.user)
