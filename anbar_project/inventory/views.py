from .models import Item
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path

# drf
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ItemSerializer

# 3rd party
import pandas as pd

import os
BASE_DIR = Path(__file__).resolve().parent.parent


def add_item(request):
    file_path = os.path.join(BASE_DIR, "/source.xlsx")
    print(f"-----------------{os.path.join(BASE_DIR, 'templates')}----------------")
    file_path = "/home/mohammadamin/Desktop/inventory_project/inventory/anbar_project/source.xlsx"
    print(file_path)
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        row_list = row.to_list()
        item = Item.objects.create(name=row_list[1], number=row_list[2],description=row_list[3],status=row_list[4])
        item.save()
    
    # return HttpResponse("Item added")
    return render(request, "inventory/add_item.html")


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
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Item.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
