from rest_framework.generics import ListCreateAPIView
from .models import Challegen
from .serializers import ChallegenListSerializer, ChallegenCreateSerializer
from .services import ChallegenService
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ChallegenListCreateView(ListCreateAPIView):
    queryset = Challegen.objects.all()
    
    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return ChallegenListSerializer
        elif self.request.method.lower() == 'post':
            return ChallegenCreateSerializer
        raise NotImplemented

    def post(self,request, *args, **kwargs):
        #valida a data
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        #call logic service
        service = ChallegenService()
        challegen = service.create(request.user,serializer.data)
        #prepare response and return
        response = ChallegenListSerializer(challegen)
        return Response(data=response.data,status=status.HTTP_201_CREATED)