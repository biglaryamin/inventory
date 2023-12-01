from django.test import TestCase, Client
from django.urls import reverse


class TestItemViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_item_index_url_successful(self):
        url = reverse('inventory:test')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)