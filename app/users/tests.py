from django.test import TestCase
from rest_framework.test import APIClient
from users.models import UserModel
from rest_framework import status
from utils.test import TestJsonStruct
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your tests here.
class UserTest(TestCase, TestJsonStruct):
    token = ''

    def setUp(self):
        user = UserModel.objects.create_user('Teste','teste@new.com','12345678')
        self.token = jwt_encode_handler(jwt_payload_handler(user))

    def test_can_login(self):
        client = APIClient()
        data = {
            'username': 'Teste',
            'password': '12345678',
        }
        response = client.post('/v1/login',data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJsonStruct(response.json(),{
            'token': str,
        })

    def test_can_register(self):
        client = APIClient()
        data = {
            'username': 'new',
            'email': 'new@new.com',
            'password': '12345678',
        }
        response = client.post('/v1/register',data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertJsonStruct(response.json(),{
            'token': str,
        })
    
    def test_can_list_users(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = client.get('/v1/users')
        self.assertJsonStruct(response.json(),{
            'results':{
                '*':{
                    'username': str,
                    'email': str,
                    'id': int
                }
            }
        })
