from django.db import models
from users.models import User
from .enuns import ChallegenStatusEnun

# Create your models here.
class Challegen(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='my_challegens')
    challenged = models.ForeignKey(User,on_delete=models.PROTECT,related_name='my_challengeds')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=ChallegenStatusEnun.OPEN)