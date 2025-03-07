from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.filter(
        stock=True,
    )
    
    return render(request, 'ecommerce/pages/home.html', {
        'page_title': 'Home',
        'products': products
    })
