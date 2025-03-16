from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.urls import reverse
from .models import Product
from reviews.models import Review
from reviews.forms import ReviewForm


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
    form = ReviewForm()
    
    product = get_object_or_404(
        Product,
        pk=id,
        stock=True
    )
    
    reviews = Review.objects.filter(
        product=product
    ).order_by('-id')
    
    # Simple Modal Creation
    modal = {
        'id': 'cartModal',
        'title': 'Added succesfully ✅',
        'text': 'This product was added to your cart.',
        'button_next': 'Go to cart',
        'url': reverse('cart:cart'),
    }

    return render(request, 'ecommerce/pages/product.html', {
        'title': f'{product.name}',
        'product': product,
        'reviews': reviews,
        'form': form,
        'modal': modal
    })


