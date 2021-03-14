from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    subscribe = models.ManyToManyField('self', symmetrical=False, related_name='subscriber')

class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wish_movie')
    title = models.CharField(max_length=100)
    num = models.IntegerField()

    def __str__(self):
        return self.title

    def __int__(self):
        return self.num
        