from django.urls import path
from . import views

urlpatterns = [
    # Customer
    path('', views.home, name='app-home'),
    path('index', views.home, name='app-home'),
    path('product', views.product, name='app-product'),
    path('order', views.order, name='app-order'),

    # Employee
    path('login', views.login, name='app.employee-login'),
    path('emp_product', views.emp_product, name='app-employee-product'),
    path('emp_ERM', views.get_name, name='app-employee-ERM')
]