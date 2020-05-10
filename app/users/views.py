from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import UserModel
from .serialisers import ListUserSerializer, LoginSerializer
from utils.pagination  import StandardResultsSetPagination

# Create your views here.
class ListUserView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = ListUserSerializer
    pagination_class = StandardResultsSetPagination