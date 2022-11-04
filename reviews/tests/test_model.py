from django.test import TestCase
from users.models import User
from videos.models import Video
from reviews.models import Review
from django.db.models import IntegerField


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "bruxo",
            "name": "Ronaldinho Gaucho",
            "password": "Ronaldo10",
            "email": "ronaldo@outlook.com",
        }

        cls.video_data_1 = {
            "title": "O BRUXO DEITA NO FRANCÊS E DIZ QUEM É O MELHOR DRIBLADOR DO FUTEBOL",
            "thumbnail": "Ronaldinho Gaúcho em entrevista em francês para a rádio RMC",
            "link": "https://youtu.be/rUSRmFp-VSA",
            "downloads": 1,
        }

        cls.data_users = {
            "name": "bruxo",
            "password": "Ronaldo10",
        }

        cls.review_data = {"text": "Vídeo ótimo!", "rating": 10}

        cls.user = User.objects.create_user(**cls.user_data)

        cls.video = Video.objects.create(**cls.video_data_1)

        cls.reviews = [
            Review.objects.create(**cls.review_data, video=cls.video, user=cls.user)
            for _ in range(10)
        ]
        cls.comentario = Review.objects.create(
            **cls.review_data, video=cls.video, user=cls.user
        )

    def test_atributes_model_video(self):
        review = self.reviews[0]
        text = review._meta.get_field("text").max_length
        rating = review._meta.get_field("rating")
        msg = [
            "Verifique se a propriedade text não excede 400 caracteres",
            "Verifique se a propriedade rating da model Review é um integer",
        ]

        self.assertEqual(text, 400, msg[0])
        self.assertTrue(isinstance(rating, IntegerField), msg[1])

    def test_multiple_reviews_can_be_attached_to_one_user(self):
        contador = 0

        for review in self.reviews:
            if review.user.id == self.user.id:
                contador = contador + 1
        self.assertEqual(len(self.reviews), contador, "erroasr")

    def test_review_fields(self):
        self.assertEqual(self.review_data["text"], self.comentario.text)
        self.assertEqual(self.review_data["rating"], self.comentario.rating)
