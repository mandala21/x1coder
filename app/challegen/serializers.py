from rest_framework import serializers
from users.serialisers import ListUserSerializer
from .models import Challegen
from users.models import User

class ChallegenListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    status = serializers.IntegerField()
    id = serializers.IntegerField()
    user = ListUserSerializer()
    challenged = ListUserSerializer()

    class Meta:
        model = Challegen
        fields = [
            'id',
            'created_at',
            'updated_at',
            'status',
            'user',
            'challenged'
        ]

class ChallegenCreateSerializer(serializers.Serializer):
    challenged_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())