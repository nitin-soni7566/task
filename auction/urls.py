from registration import views
from django.contrib import admin
from django.urls import path,include
from auction import views




urlpatterns = [
    path('',views.home),
    path('allauction',views.auction_list,name='allauctions'),
    path('adel/<int:pk>',views.auction_detail,name='auction_del'),
    path('winner',views.winner,name='winner'),
]