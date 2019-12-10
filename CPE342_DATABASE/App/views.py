from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Customer site.
def home(request):
    return render(request, 'web/index.html')

def product(request):
    product = Products.objects.all()
    return render(request, 'web/product.html', {'product': product})

def order(request):
    order = Orders.objects.all()
    return render(request, 'web/order.html', {'order': order})

# Employee site.
def emp_order(request):
    order = Orders.objects.all()
    return render(request, 'web/emp_order.html', {'order': order})

def emp_stockIn(request):
    product = Products.objects.all()
    return render(request, 'web/emp_stock-in.html', {'product': product})

def emp_customer(request):
    customer = Customers.objects.all()
    return render(request, 'web/emp_customer.html', {'customer': customer})
    
def emp_ERM(request):
    employee = Employees.objects.all()
    return render(request, 'web/emp_ERM.html', {'employee': employee})

def emp_addCoupon(request):
    return render(request, 'web/emp_add-coupon.html')

# Edit DATABASE site.
def edit_order(request):
    order = Orders.objects.filter(ordernumber = request.POST['ordernumber'])
    return render(request, 'web/edit_order.html', {'order': order})
    
def edit_stock(request):
    product = Products.objects.filter(productcode = request.POST['productcode'])
    return render(request, 'web/edit_stock.html', {'product': product})
    
def edit_customer(request):
    customer = Customers.objects.filter(customernumber = request.POST['customernumber'])
    return render(request, 'web/edit_customer.html', {'customer': customer})