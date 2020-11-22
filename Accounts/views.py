from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from django.http import JsonResponse

from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer, UserinformationSerializer, UserListSerializer, UserWishListSerializer
from .models import Wish

# Create your views here.
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def userlist(request):
    # if request.user.is_superuser:
    user = get_user_model()
    users = user.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(serializer.data)
    # return Response({'id':request.user.pk,})
    


@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserinformationSerializer(person)
    return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def wish(request, username):
#     person = get_object_or_404(get_user_model(), username=username)
#     if request.method == 'GET':
#         movie = person.wish_movie
#         serializer = UserWishListSerializer()
#     else:
#         movie_title = request.data
#         if person.wish_movie.filter(title=movie_title).exists():
#             person.wish_movie.remove(movie_title)
#         else:
#             person.wish_movie.add(movie_title)

@api_view(['GET', 'POST'])
def wish(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        wishmovie = Wish.objects.filter(user=person)
        serializer = UserWishListSerializer(wishmovie, many=True)
        return Response(serializer.data)
    # if request.method == 'POST':
    else:
        serializer = UserWishListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=person)
            return Response(serializer.data)


@api_view(['DELETE'])
def wish_delete(request, username, movie_pk):
    person = get_object_or_404(get_user_model(), username=username)
    wishmovie = Wish.objects.filter(user=person)
    deleted_movie = get_object_or_404(wishmovie, pk=movie_pk)
    deleted_movie.delete()
    return Response({'title': deleted_movie.title})