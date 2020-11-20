from django.urls import path
from . import views

urlpatterns = [
    path('nowplaying/', views.now_playing),
    path('popular/', views.popular),
    path('upcoming/', views.upcoming),
]
