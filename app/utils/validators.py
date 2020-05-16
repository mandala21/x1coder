from rest_framework import serializers

class ExistsValidator():
    def __init__(self, queryset):
        self.queryset = queryset
    
    def __call__(self, value):
        try:
            self.queryset.get(value)
        except:
            raise serializers.ValidationError('The field dont exists in datebase')
    
