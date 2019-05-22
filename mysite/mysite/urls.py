from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from tastypie.api import Api
from mySuperTrelloApp.api.resources import DescResource, CardResource

app_name = 'mainpage'


# инициализируем api
v1api = Api(api_name='api')
v1api.register(DescResource())
v1api.register(CardResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('labirint/', include('labirint.urls'), name='labirint'),
    path('twitter/', include('twitter.urls'), name='twitter'),
    path('mysupertrelloapp/', include('mySuperTrelloApp.urls')),
    path('saymyvkfriends/', include('saymyvkfriends.urls')),
    path('', include('mainpage.urls'), name='home'),
    path('', include(v1api.urls))
]
