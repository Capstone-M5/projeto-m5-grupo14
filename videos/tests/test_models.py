from rest_framework.test import APITestCase
from django.db.models import IntegerField

import ipdb
from users.models import User

from videos.models import Video

# Create your tests here.


class VideoModelTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.video_data = {
            "title": "7 Coisas",
            "thumbnail": "kajsdhkajsdhkajsdh",
            "downloads": 1
        }

        cls.user_data = {
            "username": "ricardinho",
            "name": "Ricardo Souza",
            "password": "Ricardo10",
            "email": "ricardo@outlook.com",
        }

        cls.user = User.objects.create_user(**cls.user_data)
        cls.videos = [Video.objects.create(
            **cls.video_data, link=f"http://youtube.com/adasdadasd{i}") for i in range(10)]

    def test_atributes_model_video(self):

        max_length_title = self.videos[0]._meta.get_field('title').max_length
        self.assertEqual(
            max_length_title,
            128,
            "Verifique se a propriedade title da model Video tem o tamanho max. de 128 caracteres"
        )

        type_of_downloads = self.videos[0]._meta.get_field('downloads')
        self.assertTrue(
            isinstance(type_of_downloads, IntegerField),
            "Verifique se a propriedade dowloads da model Video é um integer"
        )

    def test_user_can_be_attached_to_multiple_videos(self):

        for video in self.videos:
            self.user.videos.add(video)

        self.assertEquals(len(self.videos), self.user.videos.count())

        for video in self.videos:
            self.assertIn(self.user, video.users.all())
