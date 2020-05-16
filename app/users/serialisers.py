from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class ListUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()

class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,validators=[
        UniqueValidator(User.objects.all()),
    ])
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True,validators=[
        UniqueValidator(User.objects.all()),
    ])

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)