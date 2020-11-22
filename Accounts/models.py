from django.db import models
from django.contrib.auth.models import AbstractUser
import sys ; sys.path.append('/dir/of/movies')
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    # wish_movie = models.CharField(max_length=100)
    # like_genre = models.ManyToManyField(Genre, verbose_name='liked_user')
    # wish_movie = models.ManyToManyField(Movie, related_name='liked_user')

class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wish_movie')
    title = models.CharField(max_length=100)

#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     # wished = models.BooleanField()