from django.db import models
from users.models import User
from .enuns import ChallegenStatusEnun
from django.db import transaction
from django.db.models import Q
from random import randint
# Create your models here.
class ChallegenManager(models.Manager):
    def create(self,*args,**kwargs):
        with transaction.atomic():
            instance = super().create(*args,**kwargs)
            questions = Question.objects.get_random_questions(3)
            instance.questions.add(*questions)
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

class QuestionManager(models.Manager):
    def get_random_questions(self,number):
        results = []
        total = self.count()
        queryset = self.all()
        for i in range(0,number):
            random_id = randint(0,total - 1)
            selected = queryset[random_id]
            results.append(selected)
            queryset = queryset.exclude(id=selected.id)
            total -= 1
        return results

class Question(models.Model):
    challegen = models.ManyToManyField(Challegen,related_name='questions',blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuestionManager()