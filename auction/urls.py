from registration import views
from django.contrib import admin
from django.urls import path,include
from auction import views




urlpatterns = [
    path('',views.home),
    path('allauction',views.auction_del,name='allauctions'),
    path('adel/<int:pk>',views.auct_del,name='adel'),
    path('winner',views.winner,name='winner'),
]