from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserModel

class ListUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()

class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,validators=[
        UniqueValidator(UserModel.objects.all()),
    ])
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True,validators=[
        UniqueValidator(UserModel.objects.all()),
    ])        
    
    class Meta:
        model = UserModel
        fields = ('username','password','email')