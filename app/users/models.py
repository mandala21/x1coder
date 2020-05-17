from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import UserManager as UserBaseManager
from django.db import transaction
from django.contrib.auth.hashers import check_password

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserManager(UserBaseManager):
    def build_payload(self,user):
        return jwt_payload_handler(user)
    
    def respond_with_token(self,token):
        return {
            'token': token
        }

    def register_user(self,data):
        with transaction.atomic():
            user = self.create_user(data['username'],data['email'],data['password'])
            payload = self.build_payload(user)
            token = jwt_encode_handler(payload)
            return self.respond_with_token(token) 
    
    def get_user_from_username(self,data):
        """
        Get user from credentials informed
        """
        return User.objects.filter(Q(username=data['username'])|Q(email=data['username'])).first()
    
    def login(self,data):
        """
        Handle login in platform
        """
        user = self.get_user_from_username(data)
        if(user):
            if(check_password(data['password'],user.password)):
                payload = self.build_payload(user)
                token = jwt_encode_handler(payload)
                return self.respond_with_token(token)
        return None

# Create your models here.
class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()