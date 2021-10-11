from django.urls import path
import mypage.views

urlpatterns = [
    path('mypage_list/', mypage.views.mypage_list, name='mypage_list'),
    path('profile/delete/', mypage.views.profile_delete_view, name='profile_delete'),
    path('mypage_pwchange/', mypage.views.password_edit_view, name='mypage_pwchange'),
    path('mypage_joinlist/', mypage.views.mypage_joinlist, name='mypage_joinlist'),
    path('mypage_zzimlist/', mypage.views.mypage_zzimlist, name='mypage_zzimlist'),
    path('zzim_delete/<int:pk>/', mypage.views.zzim_delete, name='zzim_delete'),
    path('mypage_uploadlist/', mypage.views.mypage_uploadlist, name='mypage_uploadlist'),
    path('mypage_delete/<int:pk>/', mypage.views.mypage_delete, name='mypage_delete'),
    ]