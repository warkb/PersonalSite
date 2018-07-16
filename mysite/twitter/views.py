import datetime
from .models import Statement

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext, loader
from django.urls import reverse

# страшная дыра в безопасности
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    template = loader.get_template('mainpage/mainpage.html')
    twits = Statement.objects.order_by('-pub_date')
    context = RequestContext(request, {
        'twit_list': twits,
        })
    context = {'twit_list': twits,}
    response = HttpResponse(template.render(context))
    if not 'mytwit' in request.COOKIES:
        print('Кук нет')
    else:
        print('Куки есть')
        print(request.COOKIES.get('mytwit'))
    print('^_^')
    response.set_cookie('mytwit', str(datetime.datetime.now()))
    return response

@csrf_exempt
def makeNew(request):
    if request.POST['author'] and request.POST['message']:
        # если форма не пуста - добавим сообщение
        newStatement = Statement(author=request.POST['author'], 
            textOfStatement=request.POST['message'])
        newStatement.save()
    return HttpResponseRedirect(reverse('mainpage:index'))