from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('userlist/', views.userlist),
    path('<int:user_pk>/', views.profile),
    path('<int:user_pk>/wishmovie/', views.wish),
    path('<int:user_pk>/wishmovie/<int:movie_pk>/', views.wish_delete),
    path('<int:user_pk>/subscribe/', views.subscribe_list),
    path('subscribe/<int:user_pk>/', views.subscribe),
    # path('wishmovie/<title>/', views.wish),
]
