import decimal
import random

from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    stockModel = apps.get_model('stock', 'Stock')

    stocks = stockModel.objects.all()
    params = {'stocks': stocks}
    return render(request, 'dashboard.html', params)


def history(request):
    return render(request, 'history.html')


def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return redirect('dashboard')
    form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def fetchvals(request):
    if request.is_ajax():
        print('Getting latest stock prices...')

    stockModel = apps.get_model('stock', 'Stock')

    stocks = stockModel.objects.all()
    for stock in stocks:
        stock.stock_price = round(decimal.Decimal(random.uniform(-5, 5)) + stock.stock_price, 2)
        stock.save()

    data = []

    for stock in stocks:
        data.append({'stock_symbol': stock.stock_symbol, 'stock_price': stock.stock_price})

    params = {'stocks': data}
    return JsonResponse(params)


def logout(request):
    return render(request, 'logout.html')
