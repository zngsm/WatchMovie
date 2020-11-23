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
import requests

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
        # for data in datas:
        return Response(datas)
    else:
        return Response({'error': '검색결과가 없습니다'})


@api_view(['GET'])
def recommend_movie(request, movie_pk):
    url = f'https://api.themoviedb.org/3/movie/{movie_pk}/similar?api_key=8891da6c530f993ba51066b80edfa91d'
    payload = {
        'language': 'ko-kr'
    }
    res = requests.get(url, payload)
    result = res.json()["results"]
    if result:
        url_movie = f'https://api.themoviedb.org/3/movie/{result[0]["id"]}/videos?api_key=8891da6c530f993ba51066b80edfa91d'
        video = requests.get(url_movie)
        v = video.json()["results"][0]["key"]
        context = {
            "id" : result[0]["id"],
            "title" : result[0]["title"],
            "adult" : result[0]["adult"],
            "release_date" : result[0]["release_date"],
            "poster_path" : f'https://image.tmdb.org/t/p/w500{result[0]["poster_path"]}',
            "overview" : result[0]["overview"],
            "video" : f'https://www.youtube.com/embed/{v}',
        }     
    else:
        url2 = f'https://api.themoviedb.org/3/movie/{movie_pk}?api_key=8891da6c530f993ba51066b80edfa91d'
        payload = {
        'language': 'ko-kr'
        }
        err_res = requests.get(url2, payload)
        err_result = err_res.json()
        url_movie = f'https://api.themoviedb.org/3/movie/{movie_pk}/videos?api_key=8891da6c530f993ba51066b80edfa91d'
        video = requests.get(url_movie)
        v = video.json()["results"][0]["key"]

        

        context = {
            "id" : err_result["id"],
            "title" : err_result["title"],
            "adult" : err_result["adult"],
            "release_date" : err_result["release_date"],
            "poster_path" : f'https://image.tmdb.org/t/p/w500{err_result["poster_path"]}',
            "overview" : err_result["overview"],
            "video" : f'https://www.youtube.com/embed/{v}',
        }  
    return Response(context)