from rest_framework.test import APITestCase
from rest_framework.views import status

from users.models import User


class CreateVideoViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.create_video_url = "/api/video/"
        cls.video1 = {
            "link": "https://www.youtube.com/watch?v=hsZVlDQEwnI&ab_channel=LucasMeireles"
        }
        cls.video2 = {
            "link": "https://www.youtube.com/watch?v=23_qqs3mzIk&ab_channel=sasukeuchirra"
        }

    def test_can_download_video(self):
        response = self.client.post(self.create_video_url, self.video1)
        print(response.data)
        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_returning_keys(self):
        response = self.client.post(self.create_video_url, self.video1)

        expected_keys = {
            "title",
            "thumbnail",
            "link",
            "download_url",
        }

        result_keys = set(response.data.keys())

        self.assertSetEqual(expected_keys, result_keys)

    def test_list_especific_video_view(self):
        response = self.client.post(self.create_video_url, self.video1)
        videos = self.client.get(f"/api/videos/")
        video_id = videos.data.get("results")[0]["id"]
        video = self.client.get(f"{self.create_video_url}{video_id}/")
        expected_keys = {
            "id",
            "reviews",
            "title",
            "thumbnail",
            "link",
            "downloads",
        }

        result_keys = set(video.data.keys())

        self.assertSetEqual(expected_keys, result_keys)

    def test_downloads_counter(self):
        response = self.client.post(self.create_video_url, self.video1)
        videos = self.client.get(f"/api/videos/")
        video_id = videos.data.get("results")[0]["id"]
        video = self.client.get(f"{self.create_video_url}{video_id}/")

        self.assertSetEqual(4, video.data["downloads"])
