from registration import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.singup,name='singup'),
    path('login/', views.logIn,name='login'),
    path('logout/', views.logOut,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('changepass/', views.change,name='changePass'),
    path('changepass1/', views.change2,name='changePass1'),
    path('profiledit/', views.profile_edit,name='profileEdit'),
    path('users/', views.all_user,name='users'),
    path('userdel/<int:id>', views.user_del,name='userdel'),
]           