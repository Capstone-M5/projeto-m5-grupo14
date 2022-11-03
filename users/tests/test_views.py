from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token


from users.models import User


class UserViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.register_url = "/api/register/"

        cls.login_url = "/api/login/"

        cls.get_update_me_url = "/api/profile/me/"

        cls.get_soft_delete_adm_url = "/api/profile/"

        cls.user_adm = {
            "username": "adm1",
            "email": "adm@email.com",
            "password": "adm123"
        }

        cls.user_data_1 = {
            "username": "ricardinho",
            "name": "Ricardo Souza",
            "password": "Ricardo10",
            "email": "ricardo@outlook.com",
        }

        cls.user_data_2 = {
            "username": "fernandinha",
            "name": "Fernanda Lima",
            "password": "Fernanda10",
            "email": "fernanda@outlook.com",
        }

        cls.user_1_login = {
            "username": "ricardinho",
            "password": "Ricardo10"
        }

    def test_register_user(self):
        resp = self.client.post(self.register_url, self.user_data_1)

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_register_wrong(self):
        resp = self.client.post(self.register_url, data={})

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(
            resp.data["username"][0], "This field is required."
        )
        self.assertEqual(
            resp.data["name"][0], "This field is required."
        )
        self.assertEqual(
            resp.data["password"][0], "This field is required."
        )
        self.assertEqual(
            resp.data["email"][0], "This field is required."
        )

    def test_login(self):
        resp = self.client.post(self.register_url, self.user_data_1)
        resp = self.client.post(
            self.login_url, self.user_1_login)

        expected_status_code = status.HTTP_200_OK
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertIn("token", resp.data)

    def test_login_wrong(self):
        resp = self.client.post(self.register_url, self.user_data_1)
        resp = self.client.post(
            self.login_url, data={})

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(
            resp.data["username"][0], "This field is required."
        )
        self.assertEqual(
            resp.data["password"][0], "This field is required."
        )

    def test_list_profile(self):
        user = User.objects.create_user(**self.user_data_1)
        token = Token.objects.create(user=user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + token.key)

        resp = self.client.get(self.get_update_me_url)

        expected_status_code = status.HTTP_200_OK
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_update_profile(self):
        user = User.objects.create_user(**self.user_data_1)
        token = Token.objects.create(user=user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.patch(
            self.get_update_me_url, data={"name": "Ricardo Lima"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_one_user(self):
        user = User.objects.create_user(**self.user_data_1)

        resp = self.client.get(f'{self.get_soft_delete_adm_url}{user.id}/')

        expected_status_code = status.HTTP_200_OK
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)

    def test_update_is_active_by_adm(self):
        adm = User.objects.create_superuser(**self.user_adm)
        token = Token.objects.create(user=adm)
        user = User.objects.create_user(**self.user_data_1)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + token.key)

        deactive_user = {"is_active": False}

        resp = self.client.patch(
            f'{self.get_soft_delete_adm_url}{user.id}/', data=deactive_user)

        expected_status_code = status.HTTP_200_OK
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)
        self.assertEqual(resp.data["is_active"],
                         deactive_user["is_active"])

    def test_update_is_active_by_not_adm(self):
        user = User.objects.create_user(**self.user_data_1)
        token = Token.objects.create(user=user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + token.key)

        deactive_user = {"is_active": False}

        resp = self.client.patch(
            f'{self.get_soft_delete_adm_url}{user.id}/', data=deactive_user)

        expected_status_code = status.HTTP_403_FORBIDDEN
        result_status_code = resp.status_code

        self.assertEqual(expected_status_code, result_status_code)
