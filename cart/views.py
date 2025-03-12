from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ecommerce.models import Product
from utils.cart import Cart


@login_required(login_url='users:login', redirect_field_name='next')
def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quants


    return render(request, 'cart/pages/cart.html', {
        'title': 'Cart',
        'cart_products': cart_products,
        'quantities': quantities,
    })


@login_required(login_url='users:login', redirect_field_name='next')
def cart_add(request):
    # Check if we sending POST method
    if not request.POST:
        raise Http404()
    
    # Load cart
    cart = Cart(request)
    
    # Check the product_id in the value based on the script.js
    product_id = int(request.POST.get('product_id'))
    product_qty = int(request.POST.get('product_qty'))
    
    
    # Check for product in database
    product = get_object_or_404(
        Product,
        id=product_id,
        stock=True
    )
    
    # Save to session
    cart.add(product=product, quantity=product_qty)
    
    # Get cart quantity
    cart_quantity = cart.__len__()
    
    # Return response
    response = JsonResponse({
        'qty:': cart_quantity
    })
    
    return response


@login_required(login_url='users:login', redirect_field_name='next')
def cart_update(request):
    if not request.POST:
        raise Http404()
    
    cart = Cart(request)
    
    # Get stuff
    product_id = int(request.POST.get('product_id'))
    product_qty = int(request.POST.get('product_qty'))
    
    cart.update(product=product_id, quantity=product_qty)
    
    response = JsonResponse({
        'qty': product_qty
    })
    
    return response