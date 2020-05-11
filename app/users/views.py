from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import UserModel
from .serialisers import ListUserSerializer, RegisterUserSerializer
from utils.pagination  import StandardResultsSetPagination
from .service import UserService
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ListUserView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = ListUserSerializer
    pagination_class = StandardResultsSetPagination

class RegisterUserView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterUserSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = UserService()
        response = service.register_user(request.data)
        return Response(response,status=status.HTTP_201_CREATED)