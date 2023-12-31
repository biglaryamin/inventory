from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ...models import Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemDetailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)



class UploadSerializer:
    file_uploaded = serializers.FileField()

    class Meta:
        fields = ["file_uploaded"]
