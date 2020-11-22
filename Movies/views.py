from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Nowplaying, Popular, Upcoming
from .serializers import NowplayingSerializer, PopularSerializer, UpcomingSerializer

# 네이버 영화 api
import os
import sys
import urllib.request
import json

# Create your views here.
@api_view(['GET'])
def now_playing(request):
    movies = Nowplaying.objects.all()
    serializer = NowplayingSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def popular(request):
    movies = Popular.objects.all()
    serializer = PopularSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def upcoming(request):
    movies = Upcoming.objects.all()
    serializer = PopularSerializer(movies, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def search_movie(request, movie_title):
    client_id = "3OYeWxkVJzpnx_IM2YzM"
    client_secret = "aAmnOUDOTv"
    encText = urllib.parse.quote(f'{movie_title}')
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        res = response_body.decode('utf-8')
        datas = json.loads(res)["items"]
        return HttpResponse(datas)
    else:
        return Response({'error': '잘못된 접근입니다'})