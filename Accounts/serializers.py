from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Wish

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class UserinformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = ('username', 'wish_movie', 'reviews', 'comment', 'followers', 'followings')
        fields = ('username', 'wish_movie', 'reviews', 'comment', 'subscribe', 'subscriber')
        


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class UserWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ('id', 'title',)
        read_only_fields = ('user',)

class UserSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
        read_only_fields = ('id', 'username',)
