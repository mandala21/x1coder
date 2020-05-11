from .models import UserModel
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserService():
    """
    This class handle with rules of bussines layer
    """
    def register_user(self,data):
        user = UserModel.objects.create_user(data['username'],data['email'],data['password'])
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return {
            'token':token
        }  