from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from django.http import JsonResponse

from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer, UserinformationSerializer, UserListSerializer, UserWishListSerializer, UserSubscribeSerializer
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
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # serializer = UserinformationSerializer(person)
    # return Response(serializer.data)
    context = {
        'username': person.username,
    }
    # wish정보

    wi = []
    for wish in person.wish_movie.all():
        w = {}
        w['id'] = wish.num
        w['title'] = wish.title
        wi.append(w)
    context['wish_movie'] = wi

    # # reviews
    review = []
    for r in person.reviews.all():
        re_dict = {}
        re_dict['id'] = r.id
        re_dict['title'] = r.title
        review.append(re_dict)
    context['reviews'] = review

    # # comment

    c = []
    for r in person.comment.all():
        comment = {}
        comment['content'] = r.content
        comment['review_id'] = r.review.pk
        comment['review'] = r.review.title
        c.append(comment)
    context['comment'] = c

    sub = []
    for s in person.subscribe.all():
        sub_dict = {}
        sub_dict['id'] = s.id
        sub_dict['username'] = s.username
        sub.append(sub_dict)
    context['subscribe'] = sub

    subed = []
    for s in person.subscriber.all():
        sub_dict = {}
        sub_dict['id'] = s.id
        sub_dict['username'] = s.username
        subed.append(sub_dict)
    context['subscriber'] = subed

    return Response(context)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def wish(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
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
def wish_delete(request, user_pk, movie_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    wishmovie = Wish.objects.filter(user=person)
    deleted_movie = get_object_or_404(wishmovie, pk=movie_pk)
    deleted_movie.delete()
    return Response({'title': deleted_movie.title})


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def subscribe_list(request, user_pk):
    me = get_object_or_404(get_user_model(), pk=user_pk)
    # if request.method == 'GET':
    subscribe = me.subscribe
    serializer = UserSubscribeSerializer(subscribe, many=True)
    return Response(serializer.data)


@api_view(['POST', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def subscribe(request, user_pk):
    me = request.user
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
        subscribe = person.subscriber.add(me)
        serializer = UserSubscribeSerializer(subscribe, many=True)
        return Response(serializer.data)
    else:
        subscribe = person.subscriber.remove(me)
        serializer = UserSubscribeSerializer(subscribe, many=True)
        return Response(serializer.data)