from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import User
from .serialisers import ListUserSerializer, RegisterUserSerializer, LoginUserSerializer
from utils.pagination  import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ListUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    pagination_class = StandardResultsSetPagination

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = User.objects.register_user(request.data)
        return Response(response,status=status.HTTP_201_CREATED)

class LoginUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self,request,*args,**kwargs):
        #validate data
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        #call to method login
        response = User.objects.login(data)
        if(response):
            #successful login
            return Response(response,status=status.HTTP_200_OK)
        #incorrect login
        return Response({
            'message': 'Credentials are incorrect'
        },status=status.HTTP_401_UNAUTHORIZED)