from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.FloatField() # todo check attribute
    description = models.TextField()
    user = models.ForeignKey(User, related_name='products', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'title: {self.title}, price: {self.price}, description: {self.description}'

    # TODO
    # @classmethod
    # def get_for_user(cls, user):
    #     return cls.objects.filter(user=user)