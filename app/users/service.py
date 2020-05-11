from .models import UserModel
from rest_framework_jwt.settings import api_settings
from django.db import transaction

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
            user = UserModel.objects.create_user(data['username'],data['email'],data['password'])
            payload = self.build_payload(user)
            token = jwt_encode_handler(payload)
            return {
                'token':token
            } 
    
    def build_payload(self,user):
        """
        Build payload from return in login and register method
        """
        return jwt_payload_handler(user)