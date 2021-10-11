from django.urls import path, include
from .views import *

app_name = 'zeronine'

urlpatterns = [
    path('', product_in_category, name='product_all'),
    path('<category_slug>/', product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('post.urls')),
    path('product/', include('product.urls')),
    path('join/', include('join.urls')),
    path('zzim/', include('zzim.urls')),
    path('mypage/', include('mypage.urls')),
]