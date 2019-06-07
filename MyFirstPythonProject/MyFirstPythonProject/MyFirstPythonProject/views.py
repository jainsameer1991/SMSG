# I have created this file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Created by Divya")


def dashboard(request):
    return render(request, 'dashboard.html')
    # return HttpResponse("Welcome to user name")


def login(request):
    return render(request, 'login.html')
