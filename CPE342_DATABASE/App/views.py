from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from datetime import date, timedelta
from django.db.models import Q
from .models import *
from .form import *
import re
import string

user = 0

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
    return render(request, 'web/emp_customer.html', {'customer': customer, 'title': 'Emp_customer'})
    
def emp_ERM(request):
    employee = Employees.objects.get(employeenumber = '1056') # Chenge to login-user
    if(re.findall("VP", employee.jobtitle)):
        employee = Employees.objects.filter(Q(jobtitle__contains = 'Manager') | Q(jobtitle__contains = 'Rep'))
    elif(re.findall("Manager", employee.jobtitle)):
        employee = Employees.objects.filter(jobtitle__contains = 'Rep')
    else:
        return emp_customer(request)
    return render(request, 'web/emp_ERM.html', {'employee': employee,'title': 'Emp_ERM'})

def emp_mempoint(request):
    customer = Customers.objects.all()
    return render(request, 'web/emp_mempoint.html', {'customer': customer,'title': 'Emp_MemberPoint'})

def emp_pointdetail(request, question_id):
    payment = Payments.objects.filter(customernumber=question_id)
    return render(request, 'web/emp_pointdetail.html', {'payment': payment,'title': 'Emp_MemberPointDetail'})

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
        customer = Customers.objects.all()
        return render(request, 'web/emp_customer.html', {'customer': customer , 'user': user, 'title': 'Emp_customer'})
    except:
        return render(request, 'web/Login.html')

def edit_ERM(request, question_id):
    employee = Employees.objects.get(employeenumber = question_id)
    if(re.findall("Manager", employee.jobtitle)):
        context = [
            {"jobtitle": "VP"},
            {"jobtitle": "Rep"}
        ]
        return render(request, 'web/edit_ERM.html', {'employee': employee, 'change': context, 'title': 'Emp_ERM'})

    elif(re.findall("Rep", employee.jobtitle)):
        context = [
            {"jobtitle": "Manager"}
        ]
        print(context)
        return render(request, 'web/edit_ERM.html', {'employee': employee, 'change': context, 'title': 'Emp_ERM'})
    else:
        return HttpResponse("hello")

# Add site.
def add_order(request):
    product = Products.objects.all()
    return render(request, 'web/add_order.html', {'product': product, 'user': user})

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

def update_emp_order(request, question_id):
    try:
        order = Orders.objects.get(ordernumber=question_id)
        if request.POST['status'] == "Cancelled":
            order.status = "Cancelled"
            order.comments = request.POST['comments']
            order.save()
            return emp_order(request)
        if order.status == "In Process":
            orderdetails = Orderdetails.objects.filter(ordernumber=question_id)
            sum = 0
            for o in orderdetails:
                sum = sum + (o.priceeach * o.quantityordered)
            if request.POST['discountcode'] != "":
                try:
                    print(request.POST['discountcode'])
                    discount = Discountcode.objects.get(code=request.POST['discountcode'])
                    print(discount.__dict__)
                    print((discount.exp - date.today()).days)
                    if (discount.exp - date.today()).days < 0:
                        return edit_order(request, question_id)
                    sum = sum - discount.value
                except:
                    return edit_order(request, question_id)
            point = int(sum / 100) * 3
            payment = Payments(customernumber=order.customernumber,
                                checknumber=request.POST['checknumber'],
                                paymentdate=date.today(),
                                amount=sum,
                                memberpoint=point)
            if request.POST['discountcode'] != "":
                payment.discountcode = request.POST['discountcode']
                discount = Discountcode.objects.get(code=request.POST['discountcode'])
                discount.qty += -1
                discount.save()
            payment.save()
            customer = order.customernumber
            customer.totalpoint += point
            customer.save()
            order.status = "Shipped"
            order.shippeddate = date.today()
            order.save()
            return emp_order(request)
        order.status = request.POST['status']
        order.comments = request.POST['comments']
        order.save()
        return emp_order(request)
        
        
    except:
        return edit_order(request, question_id)


def add_order_to_data(request):
    try:
        order = Order.objects.get(ordernumber=request.POST['ordernumber'])
        return add_order(request)
    except:
        pass
    try:
        customer = Customers.objects.get(customernumber=request.POST['customernumber'])
        order = Orders(ordernumber=request.POST['ordernumber'],
                    orderdate=date.today(),
                    requireddate=date.today()+timedelta(10),
                    status="In Process",
                    customernumber=customer)
        i=0
        product = Products.objects.get(productcode=request.POST["productcode0"])
        product.quantityinstock += -int(request.POST["quantity" + str(i)])
        if product.quantityinstock < 0:
            return add_order(request)
        order.save()
        product.save()
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
    except:
        return add_order(request)

def update_mempoint(request):
    customer = Customers.objects.all()
    for c in customer:
        
        sum = 0
        payment = Payments.objects.filter(customernumber=c.customernumber)
        for p in payment:
            p.memberpoint = int(p.amount / 100) * 3
            sum += p.memberpoint
            p.save()
        c.totalpoint = sum
        c.save()
    return render(request, 'web/emp_mempoint.html', {'customer': customer,'title': 'Emp_MemberPoint'})

def update_ERM(request, question_id):
    employee = Employees.objects.get(employeenumber = question_id)
    if(re.findall('Manager', employee.jobtitle)):
        if(request.POST['jobtitle'] == "VP"):
            dummy = employee.jobtitle.split()
            employee.jobtitle = "VP " + dummy[0]
            try:
                employee.jobtitle += " " + dummy[2]
            except:
                print("didn't have dummy[2]")
            print(employee.jobtitle)
        else:
            dummy = employee.jobtitle.split()
            employee.jobtitle = dummy[0] + " " + "Rep"
            try:
                employee.jobtitle += " " + dummy[2]
            except:
                print("didn't have dummy[2]")
            print(employee.jobtitle)
    else:
        dummy = employee.jobtitle.split()
        employee.jobtitle = dummy[0] + " Manager"
        try:
            employee.jobtitle += " " + dummy[2]
        except:
            print("didn't have dummy[2]")
        print(employee.jobtitle)
    employee.save()

    employee = Employees.objects.get(employeenumber = '1056') # Chenge to login-user
    if(re.findall("VP", employee.jobtitle)):
        employee = Employees.objects.filter(Q(jobtitle__contains = 'Manager') | Q(jobtitle__contains = 'Rep'))
    elif(re.findall("Manager", employee.jobtitle)):
        employee = Employees.objects.filter(jobtitle__contains = 'Rep')
    else:
        return emp_customer(request)
    return render(request, 'web/emp_ERM.html', {'employee': employee,'title': 'Emp_ERM'})