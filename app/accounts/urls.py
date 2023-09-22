from accounts import views
from django.urls import path,include

urlpatterns = [
    path('', views.singup,name='singup'),
    path('login/', views.logIn,name='login'),
    path('logout/', views.logOut,name='logout'),
    path('dashbord/', views.dashbord,name='dashbord'),
    path('changepass/', views.change,name='changePass'),
    path('changepass1/', views.change2,name='changePass1'),
    path('profile/', views.profile,name='profile'),
    path('users/', views.all_user,name='users'),
    path('userdel/<int:id>', views.user_del,name='userdel'),
    path('',include('allauth.urls')),
]           