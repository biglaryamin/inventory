from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer, Serializer, FileField
from .models import Item


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']