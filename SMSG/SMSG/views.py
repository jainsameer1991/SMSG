from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hi Sameer")


def dashboard(request):
    stock1 = {'symbol': 'REL', 'price': '78.95'}
    stock2 = {'symbol': 'SBI', 'price': '85.87'}
    stock3 = {'symbol': 'REL', 'price': '78.95'}
    stock4 = {'symbol': 'SBI', 'price': '85.87'}
    stock5 = {'symbol': 'REL', 'price': '78.95'}
    stock6 = {'symbol': 'SBI', 'price': '85.87'}
    stock7 = {'symbol': 'REL', 'price': '78.95'}
    stock8 = {'symbol': 'SBI', 'price': '85.87'}
    stocks = [stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8]
    params = {'stocks': stocks}
    return render(request, 'dashboard.html', params)

def history(request):
    return render(request, 'history.html')


def login(request):
    return render(request, 'login.html')
