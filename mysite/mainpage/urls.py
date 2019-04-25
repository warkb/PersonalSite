from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = 'mainpage'
urlpatterns = [
    url(r'^saymyvkfriends', include('saymyvkfriends.urls')),
    url(r'^mysupertrelloapp', include('mySuperTrelloApp.urls')),
    url(r'^$', views.index, name='index'),
]
