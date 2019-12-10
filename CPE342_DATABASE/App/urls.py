from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Customerurl(r'^$', views.home, name='app-home'),
    url(r'^index/$', views.home, name='app-home'),
    url(r'^product/$', views.product, name='app-product'),
    url(r'^order/$', views.order, name='app-order'),

    # Employee
    url(r'^emp_order/$', views.emp_order, name='app-employee-order'),
    url(r'^emp_stock-in/$', views.emp_stockIn, name='app-employee-stockIn'),
    url(r'^emp_customer/$', views.emp_customer, name='app-employee-customer'),
    url(r'^emp_ERM/$', views.emp_ERM, name='app-employee-ERM'),
    url(r'^emp_add-coupon/$', views.emp_addCoupon, name='app-employee-addCoupon'),
    url(r'^edit_order/(?P<question_id>\d+)/$', views.edit_order, name='app-editOrder'),
    url(r'^edit_stock/(?P<question_id>\w+)/$', views.edit_stock, name='app-editStock'),
    url(r'^edit_customer/(?P<question_id>\d+)/$', views.edit_customer, name='app-editCustomer'),
]