from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# # Create your views here.
# from django.shortcuts import render, redirect
# from django.template import RequestContext, loader
# from django.urls import reverse

# # страшная дыра в безопасности
# from django.views.decorators.csrf import csrf_exempt


# # Create your views here.
# def index(request):
#     template = loader.get_template('mainpage/mainpage.html')
#     twits = Statement.objects.order_by('-pub_date')
#     context = RequestContext(request, {
#         'twit_list': twits,
#         })
#     context = {'twit_list': twits,}
#     response = HttpResponse(template.render(context))
#     if not 'mytwit' in request.COOKIES:
#         print('Кук нет')
#     else:
#         print('Куки есть')
#         print(request.COOKIES.get('mytwit'))
#     print('^_^')
#     response.set_cookie('mytwit', str(datetime.datetime.now()))
#     return response

def index(request):
    template = loader.get_template('mainpage/index.html')
    return HttpResponse(template.render())