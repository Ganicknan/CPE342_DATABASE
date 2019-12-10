from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Customer site.
def home(request):
    return render(request, 'web/index.html',{'title': 'Home'})

def product(request):
    product = Products.objects.all()
    return render(request, 'web/product.html', {'product': product,'title': 'Product'})

def order(request):
    order = Orders.objects.all()
    return render(request, 'web/order.html', {'order': order , 'title': 'Order'})

# Employee site.
def emp_order(request):
    order = Orders.objects.all()
    return render(request, 'web/emp_order.html', {'order': order , 'title': 'Emp_order'})

def emp_stockIn(request):
    product = Products.objects.all()
    return render(request, 'web/emp_stock-in.html', {'product': product , 'title': 'Emp_stockin'})

def emp_customer(request):
    customer = Customers.objects.all()
    return render(request, 'web/emp_customer.html', {'customer': customer , 'title': 'Emp_customer'})
    
def emp_ERM(request):
    employee = Employees.objects.all()
    return render(request, 'web/emp_ERM.html', {'employee': employee,'title': 'Emp_ERM'})

def emp_addCoupon(request):
    return render(request, 'web/emp_add-coupon.html' , {'title': 'addcoupon'})

# Edit DATABASE site.
def edit_order(request):
    order = Orders.objects.all()
    return render(request, 'web/edit_order.html', {'order': order , 'title': 'edit_order'})
    
def edit_stock(request):
    product = Products.objects.all()
    return render(request, 'web/edit_stock.html', {'product': product , 'title': 'edit_stock'})
    
def edit_customer(request):
    customer = Customers.objects.all()
    return render(request, 'web/edit_customer.html', {'customer': customer , 'title': 'edit_customer'})