from .models import User
from rest_framework_jwt.settings import api_settings
from django.db import transaction
from django.db.models import Q
from django.contrib.auth.hashers import check_password

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserService():
    """
    This class handle with rules of bussines layer
    """
    def register_user(self,data):
        """
        Register a new user in database
        """
        with transaction.atomic():
            user = User.objects.create_user(data['username'],data['email'],data['password'])
            payload = self.build_payload(user)
            token = jwt_encode_handler(payload)
            return self.respond_with_token(token) 
    
    def build_payload(self,user):
        """
        Build payload from return in login and register method
        """
        return jwt_payload_handler(user)

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
    
    def respond_with_token(self,token):
        """
        Handle with return data of token
        """
        return {
            'token': token
        }