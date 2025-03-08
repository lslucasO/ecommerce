from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.filter(
        stock=True,
    ).order_by('-id')
    
    return render(request, 'ecommerce/pages/home.html', {
        'page_title': 'Home',
        'products': products
    })
    

def product(request, id):
    product = Product.objects.get(
        pk=id,
        stock=True
    )
    
    return render(request, 'ecommerce/pages/product-view.html', {
        'page_title': f'{product.name}',
        'product': product
    })
