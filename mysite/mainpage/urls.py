from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'mainpage'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
