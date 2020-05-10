from rest_framework import serializers

class ListUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()