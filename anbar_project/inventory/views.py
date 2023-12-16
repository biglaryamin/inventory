from .models import Item
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pathlib import Path
from .forms import FileUploadForm
from django.contrib import messages

# drf
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ItemSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from .serializers import UploadSerializer

# 3rd party
import pandas as pd

import os

BASE_DIR = Path(__file__).resolve().parent.parent
from rest_framework.viewsets import ViewSet

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import Item
import pandas as pd


def add_item(request):
    form = FileUploadForm()

    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data["file"]

            try:
                df = pd.read_excel(uploaded_file)

                for _, row in df.iterrows():
                    name = row[1]
                    number = row[2]
                    description = row[3]
                    status = row[4]

                    # Check if a similar item already exists
                    if Item.objects.filter(
                        name=name, number=number, status=status
                    ).exists():
                        messages.warning(
                            request,
                            f"Item with name: {name}, number: {number}, status: {status} already exists. Skipping.",
                        )
                        continue

                    # If not, add the item
                    item = Item.objects.create(
                        name=name, number=number, description=description, status=status
                    )
                    item.save()

                messages.success(request, "Items saved successfully")
            except Exception as e:
                messages.error(
                    request, f"Something went wrong with your file: {str(e)}"
                )
        else:
            messages.error(request, "Form is not valid.")

    return render(request, "inventory/add_item.html", {"form": form})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Other actions for CRUD operations

    @action(detail=False, methods=['post'], url_path='item')
    @csrf_exempt
    def add_item(self, request):
        try:
            uploaded_file = request.data['file']
            df = pd.read_excel(uploaded_file)
            print(df)

            for _, row in df.iterrows():
                name = row.iloc[1]
                number = row.iloc[2]
                description = row.iloc[3]
                status = row.iloc[4]

                if Item.objects.filter(name=name, number=number, status=status).exists():
                    messages.warning(
                        request,
                        f"Item with name: {name}, number: {number}, status: {status} already exists. Skipping.",
                    )
                    continue

                item = Item.objects.create(
                    name=name, number=number, description=description, status=status
                )
                item.save()

            messages.success(request, "Items saved successfully")
            return Response({"message": "Items saved successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            messages.error(request, f"Something went wrong with your file: {str(e)}")
            return Response({"error": f"Something went wrong with your file: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        return Response("GET API")
    
    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        df = pd.read_excel(file_uploaded)

        for _, row in df.iterrows():
            name = row.iloc[1]
            number = row.iloc[2]
            description = row.iloc[3]
            status = row.iloc[4]

            if Item.objects.filter(name=name, number=number, status=status).exists():
                messages.warning(
                    request,
                    f"Item with name: {name}, number: {number}, status: {status} already exists. Skipping.",
                )
                continue

            item = Item.objects.create(
                name=name, number=number, description=description, status=status
            )
            item.save()

        content_type = file_uploaded.content_type
        response = "POST API and you havee uploaded a {} file".format(content_type)
        return Response(response)