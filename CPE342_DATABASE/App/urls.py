from django.urls import path
from . import views

urlpatterns = [
    # Customer
    path('', views.home, name='app-home'),
    path('index.html', views.home, name='app-home'),
    path('product.html', views.product, name='app-product'),
    path('order.html', views.order, name='app-order'),

    # Employee
    path('emp_order.html', views.emp_order, name='app-employee-order'),
    path('emp_stock-in.html', views.emp_stockIn, name='app-employee-stockIn'),
    path('emp_customer.html', views.emp_customer, name='app-employee-customer'),
    path('emp_ERM.html', views.emp_ERM, name='app-employee-ERM'),
    path('emp_add-coupon.html', views.emp_addCoupon, name='app-employee-addCoupon'),
    path('order/edit_order.html', views.edit_order, name='app-editOrder'),
    path('product/edit_stock.html', views.edit_stock, name='app-editStock'),
    path('customer/edit_customer.html', views.edit_customer, name='app-editCustomer'),
]