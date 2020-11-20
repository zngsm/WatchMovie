from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list_create),
    path('<int:pk>/', views.review_update_delete),
    path('<int:pk>/comment/', views.comment),
    path('<int:pk>/comment/<int:comment_pk>', views.comment_update_delete),
    # path('<int:pk>/like/', views.like),
]