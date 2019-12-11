from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *

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
    try:
        coupon = Discountcode(code=request.POST['code'], value=request.POST['value'], exp=request.POST['exp'], qty=request.POST['qty'])
        coupon.save()
    except:
        pass
    return render(request, 'web/emp_add-coupon.html' , {'title': 'addcoupon'})

# Edit DATABASE site.
def edit_order(request, question_id):
    order = Orders.objects.get(ordernumber = question_id)
    orderdetail = Orderdetails.objects.filter(ordernumber = question_id)
    for p in orderdetail:
        print(p.ordernumber)
    return render(request, 'web/edit_order.html', {'order': order, 'orderdetail': orderdetail, 'title': 'edit_order'})
    
def edit_stock(request, question_id):
    product = Products.objects.filter(productcode = question_id)
    return render(request, 'web/edit_stock.html', {'product': product, 'title': 'edit_stock'})
    
def edit_customer(request, question_id):
    customer = Customers.objects.filter(customernumber = question_id)
    return render(request, 'web/edit_customer.html', {'customer': customer, 'title': 'edit_customer'})

def login(request):
    return render(request, 'web/Login.html')

def get_name(request):
    try:
        password = (int(request.POST['password']) + 1234567890) * 76
        user = Employees.objects.get(employeenumber = request.POST['username'])
        if password != int(user.password):
            return render(request, 'web/Login.html')
        return render(request, 'web/emp_ERM.html', {'user': user})
    except:
        return render(request, 'web/Login.html')
