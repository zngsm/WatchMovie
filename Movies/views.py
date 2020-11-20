from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Nowplaying, Popular, Upcoming
from .serializers import NowplayingSerializer, PopularSerializer, UpcomingSerializer
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
    return Response(serializer.data)