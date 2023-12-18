from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from inventory.models import Item



class YourAppViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for authentication in your views
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.group = Group.objects.create(name='testgroup')
        self.item = Item.objects.create(name='Test Item', number='123', description='Test Description', status='Active')

        # Create an API client
        self.client = APIClient()

    def test_user_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Test the UserViewSet
        response = self.client.get('http://127.0.0.1:8000/users/')  # Replace with your actual endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed

    def test_group_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Test the GroupViewSet
        response = self.client.get('http://127.0.0.1:8000/groups/')  # Replace with your actual endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed

    def test_item_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Test the ItemViewSet
        response = self.client.get('http://127.0.0.1:8000/items/')  # Replace with your actual endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed

    def test_upload_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Test the UploadViewSet
        response = self.client.post('http://127.0.0.1:8000/uploads/', data={'file_uploaded': '/home/mohammadamin/Desktop/inventory_project/inventory/anbar_project/source.xlsx'})  # Replace with your actual endpoint and file content
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed
