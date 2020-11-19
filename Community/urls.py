from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list_create),
    path('<int:pk>/', views.review_update_delete),
    path('<int:pk>/like/', views.like),
]
