from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'mySuperTrelloApp'

urlpatterns = [
    path('', views.mainpage, name='maintrellopage'),
    path('get_descs', views.get_descs, name='get_descs')
]
