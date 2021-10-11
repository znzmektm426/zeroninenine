from django.urls import path
from .views import *

urlpatterns = [
    path('join_create/<int:id>/', join_create, name='join_create'),
    ]