from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('post/', views.post_details, name='post_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
