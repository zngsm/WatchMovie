from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('userlist/', views.userlist),
    path('<username>/', views.profile),
    path('<username>/wishmovie/', views.wish),
    path('<username>/wishmovie/<int:movie_pk>/', views.wish_delete),
    # path('wishmovie/<title>/', views.wish),
]
