from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('userlist/', views.userlist),
    path('wishmovie/<title>/', views.wish),
    path('<username>/', views.profile),
    
]
