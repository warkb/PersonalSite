from django.contrib import admin
from django.conf.urls import url, include
from . import views
app_name = 'labirint'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
