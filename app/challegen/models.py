from django.db import models
from users.models import User
from .enuns import ChallegenStatusEnun
from django.db import transaction
from django.db.models import Q
# Create your models here.
class ChallegenManager(models.Manager):
    def create(self,*args,**kwargs):
        with transaction.atomic():
            instance = super().create(*args,**kwargs)
            return instance
    
    def get_user_challegens(self,user):
        return super().get_queryset().filter(Q(user=user)|Q(challenged=user))


class Challegen(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='my_challegens')
    challenged = models.ForeignKey(User,on_delete=models.PROTECT,related_name='my_challengeds')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=ChallegenStatusEnun.OPEN)
    winner = models.ForeignKey(User,on_delete=models.PROTECT,related_name='victories',default=None,null=True,blank=True)
    
    objects = ChallegenManager()