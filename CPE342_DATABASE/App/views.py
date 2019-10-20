from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'web/index.html')

def product(request):
    product = Products.objects.all()
    return render(request, 'web/product.html', {'product': product})