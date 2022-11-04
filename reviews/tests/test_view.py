from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from users.models import User


class CreateReviewViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.create_video_url = "/api/video/"
        cls.video1 = {
            "link": "https://www.youtube.com/watch?v=hsZVlDQEwnI&ab_channel=LucasMeireles"
        }

        cls.review_data = {
            "text": "Cosinha mais fofa o gatinho miando S2",
            "rating": 10
        }
        user_data = {
            "name": "lucas",
            "username": "lucas1",
            "email": "lucas@mail.com",
            "password": "Kenzinha10"
        }
        cls.user = User.objects.create_user(**user_data)
        cls.user_token = Token.objects.get_or_create(user=cls.user)[0].key

    def test_user_can_create_review(self):
        self.client.post(self.create_video_url, self.video1)
        videos = self.client.get("/api/videos/")
        self.video_id = videos.data.get("results")[0]["id"]
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.post(
            f"/api/video/{self.video_id}/review/", self.review_data)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_returning_keys(self):
        self.client.post(self.create_video_url, self.video1)
        videos = self.client.get("/api/videos/")
        self.video_id = videos.data.get("results")[0]["id"]
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.post(
            f"/api/video/{self.video_id}/review/", self.review_data)

        expected_keys = {
            "id",
            "video",
            "text",
            "rating",
            "created_at",
            "user",
        }

        result_keys = set(response.data.keys())

        self.assertSetEqual(expected_keys, result_keys)

    def test_cannot_create_review_not_authenticated(self):
        self.client.post(self.create_video_url, self.video1)
        videos = self.client.get("/api/videos/")
        self.video_id = videos.data.get("results")[0]["id"]
        response = self.client.post(
            f"/api/video/{self.video_id}/review/", self.review_data)

        expected_status_code = status.HTTP_401_UNAUTHORIZED
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_cannot_create_with_invalid_video_id(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.post(
            f"/api/video/dasfdasf/review/", self.review_data)

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_cannot_create_with_non_existent_video_id(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.post(
            f"/api/video/0af540bb-51a5-4bd8-97cb-9532e4edb750/review/", self.review_data)

        expected_status_code = status.HTTP_404_NOT_FOUND
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_cannot_create_with_invalid_rating(self):
        self.client.post(self.create_video_url, self.video1)
        videos = self.client.get("/api/videos/")
        self.video_id = videos.data.get("results")[0]["id"]
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.post(
            f"/api/video/{self.video_id}/review/", {
                "text": "Cosinha mais fofa o gatinho miando S2",
                "rating": 11  # permite apenas de 1 a 10
            })

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)
