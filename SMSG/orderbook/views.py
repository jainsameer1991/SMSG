import random
import time
from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Order


def orderbook(request):
    orders = Order.objects.all()
    params = {'orders': orders}
    return render(request, 'orderbook.html', params)

def registerorder(request):
    print("In server...")
    symbol = request.GET.get('symbol')
    quantity = request.GET.get('quantity')
    price = request.GET.get('price')
    # Order.objects.create(symbol, quantity, price)
    # order.save()
    order = Order(order_symbol=symbol, order_type='BUY', order_quantity=int(quantity),
                  order_price=round(Decimal(price), 2), order_status='OPEN')
    order.save()
    print(price)
    return JsonResponse({'success': True})
