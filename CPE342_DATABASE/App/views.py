from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'web/index.html')

def product(request):
    product = Products.objects.all()
    return render(request, 'web/product.html', {'product': product})

def order(request):
    order = Orders.objects.all()
    return render(request, 'web/order.html', {'order': order})

def emp_product(request):
    product = Products.objects.all()
    return render(request, 'web/emp_product.html', {'product': product})