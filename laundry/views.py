from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json

# Create your views here.
def Dashboard(request):
    return render(request, 'laundry/dashboard.html')

def Pos(request):
    laundry = Laundry.objects.all()
    """if request.user.is_authenticated:
        order, created = Order.objects.get_or_create()
        item = order.OrderItem_set.all()
    else:
        order = []"""
    
        
    
    

    context = {
        'laundry':laundry,
        #'item':item,
        
    }
    return render(request, 'laundry/pos.html', context)

def Pickup(request):
    return render(request, 'laundry/pickup.html')

def SalesRecord(request):
    return render(request, 'laundry/records.html')

def CheckoutDetails(request):
    laundry = Laundry.objects.all()
    item = OrderItem.objects.all()
    order = Order.objects.all()

    cart_total = sum({item.quantity for item in item})
    price_total = sum({item.get_total for item in item})

    context = {
        'price_total':price_total,
        'cart_total':cart_total,
        'order':order,
        'laundry':laundry,
        'item':item,
    }
    return render(request, 'laundry/cart.html', context)

def Checkout(request):

    return render(request, 'laundry/checkout.html')


def updateItem(request):
    data = json.loads(request.body)
    laundryId = data['laundryId']
    action = data['action']
    
    print('Action:', action)
    print('laundryId:', laundryId)
    
    laundry = Laundry.objects.get(id=laundryId)
    item = OrderItem.objects.get(id=laundryId)
    order = Order.objects.get(id=laundryId)
    
    if action == 'add':
        item.quantity = (item.quantity + 1)
    elif action == 'remove':
        item.quantity = (item.quantity - 1)
        
    item.save()
    
    if item.quantity <= 0:
        item.delete()
        
    context = {
        'order':order,
        'laundry':laundry,
        'item':item,
    }
    
    return JsonResponse('Item was added', context, safe=False)
