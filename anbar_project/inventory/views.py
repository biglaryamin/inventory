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

# 3rd party
import pandas as pd

import os
BASE_DIR = Path(__file__).resolve().parent.parent


from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import Item
import pandas as pd



def add_item(request):
    form = FileUploadForm()

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data['file']

            try:
                df = pd.read_excel(uploaded_file)

                for _, row in df.iterrows():
                    name = row[1]
                    number = row[2]
                    description = row[3]
                    status = row[4]

                    # Check if a similar item already exists
                    if Item.objects.filter(name=name, number=number, status=status).exists():
                        messages.warning(request, f"Item with name: {name}, number: {number}, status: {status} already exists. Skipping.")
                        continue

                    # If not, add the item
                    item = Item.objects.create(
                        name=name,
                        number=number,
                        description=description,
                        status=status
                    )
                    item.save()

                messages.success(request, "Items saved successfully")
            except Exception as e:
                messages.error(request, f"Something went wrong with your file: {str(e)}")
        else:
            messages.error(request, "Form is not valid.")

    return render(request, "inventory/add_item.html", {'form': form})



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
