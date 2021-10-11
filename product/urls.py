from django.urls import path
from .views import *

urlpatterns = [
    path('product_upload/', product_upload, name='product_upload'),
    path('product_search/', product_search, name='product_search'),
    ]