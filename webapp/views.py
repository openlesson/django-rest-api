from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def hello(request):
    print('Method', request.method)
    print('Headers', request.headers)
    print('Body', request.body)
    return HttpResponse('<h1>Hello Django World!</h1><p>It is very easy!</p>')
