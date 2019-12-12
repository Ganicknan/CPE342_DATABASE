from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Customer
    url(r'^$', views.home, name='app-home'),
    url(r'^index/$', views.home, name='app-home'),
    url(r'^product/$', views.product, name='app-product'),
    url(r'^order/$', views.order, name='app-order'),

    # Employee
    url(r'^login/$', views.login, name='app-login'),
    url(r'^get_login/$', views.get_name, name='app-getlogin'),
    url(r'^emp_order/$', views.emp_order, name='app-employee-order'),
    url(r'^emp_stock-in/$', views.emp_stockIn, name='app-employee-stockIn'),
    url(r'^emp_customer/$', views.emp_customer, name='app-employee-customer'),
    url(r'^emp_ERM/$', views.emp_ERM, name='app-employee-ERM'),
    url(r'^edit_ERM/(?P<question_id>\d+)/$', views.edit_ERM, name='app-editERM'),
    url(r'^emp_add-coupon/$', views.emp_addCoupon, name='app-employee-addCoupon'),
    url(r'^update_emp_order/(?P<question_id>\d+)/$', views.update_emp_order, name='app-editOrder'),
    url(r'^update_ERM/(?P<question_id>\d+)/$', views.update_ERM, name='app-updateERM'),
    url(r'^edit_order/(?P<question_id>\d+)/$', views.edit_order, name='app-editOrder'),
    url(r'^update_emp_stock/(?P<question_id>\w+)/$', views.update_emp_product, name='app-editStock-update'),
    url(r'^delete_emp_stock/(?P<question_id>\w+)/$', views.delete_product, name='app-deleteStock'),
    url(r'^edit_stock/(?P<question_id>\w+)/$', views.edit_stock, name='app-editStock'),
    url(r'^update_emp_customer/(?P<question_id>\w+)/$', views.update_emp_customer, name='update_customer'),
    url(r'^edit_customer/(?P<question_id>\d+)/$', views.edit_customer, name='app-editCustomer'),
    url(r'^add_order/$', views.add_order, name='app-addOrder'),
    url(r'^add_order_to_database/$', views.add_order_to_data, name='app-addOrder-to-database'),
    url(r'^add_stock/$', views.add_stock, name='app-addStock'),
    url(r'^add_stock_to_database/$', views.add_product_to_data, name='app-addStock-to-database'),
    url(r'^add_customer/$', views.add_customer, name='app-addCustomer'),
    url(r'^add_customer_to_database/$', views.add_customer_to_data, name='app-addCustomer-to-database'),
    url(r'^emp_mempoint/$', views.emp_mempoint, name='app-mempoint'),
    url(r'^emp_mempoint/(?P<question_id>\w+)/$', views.emp_pointdetail, name='app-detail'),
    url(r'^emp_pointupdate/$', views.update_mempoint, name='app-update-mempoint'),
]
