from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class SegstreamAPILogsAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_apilogs_get_logs_list(self):
        url = "/api/v1/api-logs/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

