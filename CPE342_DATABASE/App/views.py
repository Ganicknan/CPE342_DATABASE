from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *

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

def login(request):
    return render(request, 'web/Login.html')

def emp(request):
    return render(request, 'web/emp_ERM.html')

def get_name(request):
    try:
        password = (int(request.POST['password']) + 1234567890) * 76
        user = Employees.objects.get(employeenumber = request.POST['username'])
        if password != int(user.password):
            return render(request, 'web/Login.html')
        return render(request, 'web/emp_ERM.html', {'user': user})
    except:
        return render(request, 'web/Login.html')