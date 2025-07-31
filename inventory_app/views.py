from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def product_list(request):
    in_stock = Product.objects.filter(in_stock=True)
    out_stock = Product.objects.filter(in_stock=False)
    products = Product.objects.all()
    return render(request, 'inventory_app/product_list.html', {'products': products})

   



