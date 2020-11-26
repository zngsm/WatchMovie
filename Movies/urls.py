from django.urls import path
from . import views

urlpatterns = [
    path('nowplaying/', views.now_playing),
    path('popular/', views.popular),
    path('upcoming/', views.upcoming),
    path('search/<movie_title>/', views.search_movie),
    path('recommend/<int:movie_pk>/', views.recommend_movie),
    path('genres/<int:genre_pk>/', views.genres),
]
