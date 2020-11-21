from django.db import models
from django.contrib.auth.models import AbstractUser
# import sys ; sys.path.append('/dir/of/movies')
# from movies.models import Genre

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    wish_movie = models.CharField(max_length=100)
    # like_genre = models.ManyToManyField(Genre, verbose_name='liked_user')
    # wish_movie = models.ManyToManyField(Movie, verbose_name='liked_user')
