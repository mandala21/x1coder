from django.test import TestCase
from rest_framework.test import APIClient
from users.models import UserModel
from rest_framework import status
from utils.test import TestJsonStruct

# Create your tests here.
class UserTest(TestCase, TestJsonStruct):

    def setUp(self):
        UserModel.objects.create_user('Teste','teste@new.com','12345678')

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
