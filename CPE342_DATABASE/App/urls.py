from django.urls import path
from . import views

urlpatterns = [
    # Customer
    path('', views.home, name='app-home'),
    path('index.html', views.home, name='app-home'),
    path('product.html', views.product, name='app-product'),
    path('order.html', views.order, name='app-order'),

    # Employee
    path('emp_product.html', views.emp_product, name='app-employee-product')
]