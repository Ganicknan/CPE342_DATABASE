from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('index.html', views.home, name='app-home'),
    path('product.html', views.product, name='app-product'),
    path('order.html', views.order, name='all-order')
]