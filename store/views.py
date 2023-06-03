from django.shortcuts import render

from .models import Product, Category

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
