from django.urls import path
from . import views

urlpatterns = [
    # Customer
    path('', views.home, name='app-home'),
    path('index.html', views.home, name='app-home'),
    path('product.html', views.product, name='app-product'),
    path('order.html', views.order, name='app-order'),

    # Employee
    path('login.html', views.login, name='app.employee-login'),
    path('emp_product.html', views.emp_product, name='app-employee-product'),
    path('emp_ERM.html', views.get_name, name='app-employee-ERM')
]