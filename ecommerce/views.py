from django.shortcuts import render
from django.db.models import Q
from .models import Product



def home(request):
    products = Product.objects.filter(
        stock=True,
    ).order_by('-id')
    
    return render(request, 'ecommerce/pages/home.html', {
        'title': 'Home',
        'products': products
    })
    

def search(request):
    search_term = request.GET.get('q')
    
    product = Product.objects.filter(
        Q(name__icontains=search_term) |
        Q(slug__icontains=search_term)
    )
    
    return render(request, 'ecommerce/pages/search-view.html', {
        'title': f'Search | {search_term}',
        'products': product,
    })


def product(request, id):
    product = Product.objects.get(
        pk=id,
        stock=True
    )
    
    return render(request, 'ecommerce/pages/product.html', {
        'title': f'{product.name}',
        'product': product
    })


