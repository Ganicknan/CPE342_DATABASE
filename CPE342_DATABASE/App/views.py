from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, timedelta
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
    product = Products.objects.get(productcode = question_id)
    return render(request, 'web/edit_stock.html', {'product': product, 'title': 'edit_stock'})
    
def edit_customer(request, question_id):
    customer = Customers.objects.get(customernumber = question_id)
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
# Add site.
def add_order(request):
    product = Products.objects.all()
    return render(request, 'web/add_order.html', {'product': product})

def add_stock(request):
    return render(request, 'web/add_stock.html')
    
def add_customer(request):
    return render(request, 'web/add_customer.html')

#POST method
def update_emp_customer(request, question_id):
    try:
        customer = Customers.objects.get(customernumber = question_id)
        customer.customername = request.POST['customername']
        customer.contactlastname = request.POST['contactlastname']
        customer.contactfirstname = request.POST['contactfirstname']
        customer.phone = request.POST['phone']
        customer.addressline1 = request.POST['addressline1']
        customer.addressline2 = request.POST['addressline2']
        customer.city = request.POST['city']
        customer.state = request.POST['state']
        customer.postalcode = request.POST['postalcode']
        customer.country = request.POST['country']
        customer.salesrepemployeenumber = Employees.objects.get(employeenumber=request.POST['salesrepemployeenumber'])
        customer.save()
        customer = Customers.objects.all()
        return render(request, 'web/emp_customer.html', {'customer': customer})
    except:
        return edit_customer(request, question_id)

def add_customer_to_data(request):
    try:
        cus = Customers.objects.get(customernumber=request.POST['customernumber'])
        return add_customer(request)
    except:
        pass
    try:
        emp = Employees.objects.get(employeenumber=request.POST['salesrepemployeenumber'])
        customer = Customers(customernumber = request.POST['customernumber'], 
                            customername = request.POST['customername'],
                            contactlastname = request.POST['contactlastname'],
                            contactfirstname = request.POST['contactfirstname'],
                            phone = request.POST['phone'],
                            addressline1 = request.POST['addressline1'],
                            addressline2 = request.POST['addressline2'],
                            city = request.POST['city'],
                            state = request.POST['state'],
                            postalcode = request.POST['postalcode'],
                            country = request.POST['country'],
                            salesrepemployeenumber = emp,
                            creditlimit = request.POST['creditlimit'],
                            totalpoint = 0)
        print(customer.__dict__)
        customer.save()
    except:
        return add_customer(request)
    return emp_customer(request)

def update_emp_product(request, question_id):
    try:
        product = Products.objects.get(productcode = question_id)
        product.productname = request.POST['productname']
        product.productline = Productlines.objects.get(productline= request.POST['productline'])
        product.productscale = request.POST['productscale']
        product.productvendor = request.POST['productvendor']
        product.productdescription = request.POST['description']
        product.quantityinstock = request.POST['quantity']
        product.buyprice = request.POST['price']
        product.msrp = request.POST['msrp']
        product.save()
        return emp_stockIn(request)
    except:
        return edit_stock(request, question_id)

def add_product_to_data(request):
    try:
        pro = Products.objects.get(productcode=request.POST['productcode'])

        return add_stock(request)
    except:
        pass
    try:
        productline = Productlines.objects.get(productline= request.POST['productline'])
        product = Products(productcode = request.POST['productcode'], 
                            productname = request.POST['productname'],
                            productline = productline,
                            productscale = request.POST['productscale'],
                            productvendor = request.POST['productvendor'],
                            productdescription = request.POST['description'],
                            quantityinstock = request.POST['quantity'],
                            buyprice = request.POST['price'],
                            msrp = request.POST['msrp'])
        product.save()
    except:
        return add_stock(request)
    return emp_stockIn(request)

def delete_product(request, question_id):
    try:
        product = Products.objects.get(productcode=question_id)
        product.delete()
        return emp_stockIn(request)
    except:
        return edit_stock(request, question_id)

def add_order_to_data(request):
    try:
        order = Order.objects.get(ordernumber=request.POST['ordernumber'])
        return add_order(request)
    except:
        pass
    #try:
    customer = Customers.objects.get(customernumber=request.POST['customernumber'])
    order = Orders(ordernumber=request.POST['ordernumber'],
                orderdate=date.today(),
                requireddate=date.today()+timedelta(10),
                status="In Process",
                customernumber=customer)
    order.save()
    i=0
    try:
        
        while True:
            product = Products.objects.get(productcode=request.POST["productcode" + str(i)])
            orderdetail = Orderdetails(ordernumber=order,
                                        productcode=product,
                                        quantityordered=request.POST["quantity" + str(i)],
                                        priceeach=product.buyprice,
                                        orderlinenumber=i+1)
            orderdetail.save()
            i+=1
            #Orders.objects.get(ordernumber=10100)
    except:
        print(i)
    return emp_order(request)
    #except:
        #return add_order(request)