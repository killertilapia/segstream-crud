from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

# Create your tests here.

User = get_user_model()


class SegstreamUserAPITests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user_data = {
            "username": "rob_zombie",
            "email": "dragula@hellbilly.dlx",
            "password": "test_password",
            "first_name": "Rob",
            "last_name": "Zombie"
        }
        
        User.objects.create_user(**user_data)

    def setUp(self):
        self.client = APIClient()

    def test_myusers_users_sanity_check(self):
        result_set = User.objects.filter(email="dragula@hellbilly.dlx")
        self.assertIsNotNone(result_set)
        self.assertEqual(1, result_set.count())


    def test_myusers_get_user_list(self):
        url = "/api/v1/users/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("Rob", response.data[0]['first_name'])
        self.assertEqual("Zombie", response.data[0]['last_name'])

    def test_myusers_get_user_id(self):
        url = "/api/v1/users/1/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("Rob", response.data['first_name'])
        self.assertEqual("Zombie", response.data['last_name'])

    def test_myusers_post_add_user(self):
        url = "/api/v1/users/"

        user_data = {
            "password": "pass",
            "username": "new_user",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test_email@test.org"
        }

        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual("John", response.data['first_name'])
        self.assertEqual("Doe", response.data['last_name'])
        self.assertEqual("test_email@test.org", response.data['email'])

    def test_myusers_put_replace_user(self):
        url = "/api/v1/users/1/"

        user_data = {
            "password": "pass",
            "username": "replace_user",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test_email@test.org"
        }

        response = self.client.put(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("John", response.data['first_name'])
        self.assertEqual("Doe", response.data['last_name'])
        self.assertEqual("replace_user", response.data['username'])

    def test_myusers_patch_update_user(self):
        url = "/api/v1/users/1/"

        user_data = {
            "username": "replace_user",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test_email@test.org"
        }

        response = self.client.patch(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("John", response.data['first_name'])
        self.assertEqual("Doe", response.data['last_name'])
        self.assertEqual("replace_user", response.data['username'])