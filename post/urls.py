from django.urls import path
from .views import *

urlpatterns = [
    path('post/', post, name='post'),
    path('post_write/', post_write, name='post_write'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
    path('post_delete/<int:pk>/', post_delete, name='post_delete'),
    path('post_modify/<int:pk>/', post_modify, name='post_modify'),
    path('comment_create/<int:article_pk>', comment_create, name='comment_create'),
    path('comment_delete/<int:comment_pk>', comment_delete, name='comment_delete'),
    path('search/', search, name='search'),
]