from tastypie.resources import ModelResource
from mySuperTrelloApp.models import Desc, Card

class DescResource(ModelResource):
    class Meta:
        queryset = Desc.objects.all()
        allowed_methods = ['get']

class CardResource(ModelResource):
    class Meta:
        queryset = Card.objects.all()
        allowed_methods = ['get']

