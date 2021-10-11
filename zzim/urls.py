from django.urls import path
from .views import *
import zzim.views

urlpatterns = [
    path('zzim/', zzim.views.zzim, name='zzim'),
    path('add_zzim/<int:id>/', add_zzim, name='add_zzim'),
    ]