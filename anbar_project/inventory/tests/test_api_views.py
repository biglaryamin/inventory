from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from inventory.models import Item

import os
from django.core.files.uploadedfile import SimpleUploadedFile

file_path = (
    "/home/mohammadamin/Desktop/inventory_project/inventory/anbar_project/source.xlsx"
)


class InventoryAppViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for authentication in your views
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.group = Group.objects.create(name="testgroup")
        self.item = Item.objects.create(
            name="Test Item",
            number="123",
            description="Test Description",
            status="n",
        )

        # Create an API client
        self.client = APIClient()

    def test_user_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Test the UserViewSet
        response = self.client.get(
            "http://127.0.0.1:8000/users/"
        )  # Replace with your actual endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed

    def test_group_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Test the GroupViewSet
        response = self.client.get(
            "http://127.0.0.1:8000/groups/"
        )  # Replace with your actual endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed

    def test_item_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Test the ItemViewSet
        response = self.client.get(
            "http://127.0.0.1:8000/items/"
        )  # Replace with your actual endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed

    def test_upload_viewset(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Prepare the file for upload

        with open(file_path, "rb") as file:
            file_content = file.read()
            file_name = os.path.basename(file_path)

            uploaded_file = SimpleUploadedFile(file_name, file_content)

            # Test the UploadViewSet
            response = self.client.post(
                "http://127.0.0.1:8000/upload/", {"file_uploaded": uploaded_file}
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more test cases as needed

    def test_upload_viewset_duplicate_items(self):
        # Log in the user
        self.client.force_authenticate(user=self.user)

        # Prepare a file with duplicate items for upload

        with open(file_path, "rb") as file:
            file_content = file.read()
            file_name = os.path.basename(file_path)

            uploaded_file = SimpleUploadedFile(file_name, file_content)

            # Test the UploadViewSet
            response = self.client.post(
                "http://127.0.0.1:8000/upload/", {"file_uploaded": uploaded_file}
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the database to verify that duplicate items were not created
        self.assertEqual(Item.objects.count(), 5)
