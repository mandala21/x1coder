from .models import Challegen

class ChallegenService():
    """
    Logic bussines for challegen
    """

    def create(self,user,data):
        data['user'] = user
        return Challegen.objects.create(**data)