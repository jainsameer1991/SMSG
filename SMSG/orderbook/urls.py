from django.urls import path
from . import views

urlpatterns = [
    path('', views.orderbook, name='orderbook'),
    path('registerorder/', views.registerorder, name='registerorder')
]
