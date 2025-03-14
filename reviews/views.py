from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ReviewForm
from django.contrib import messages
from ecommerce.models import Product  # Import the Product model
from django.contrib.auth.models import User  # Import the User model


def create(request):
    if not request.POST:
        raise Http404()
    
    # Retrieve the product ID from the request (e.g., via POST data or URL parameter)
    product_id = request.POST.get('product_id')  # Assuming you pass it via a hidden input
    product = get_object_or_404(Product, id=product_id)
    
    # Create the form instance with the submitted data
    form = ReviewForm(request.POST)
    
    if form.is_valid():
        # Save the form without committing to the database
        review = form.save(commit=False)
        
        # Set the user and product fields programmatically
        review.user = request.user  # Assuming the user is logged in
        review.product = product
        
        # Save the review to the database
        review.save()
        
        messages.success(request, 'Your review was created.')
    else:
        messages.error(request, 'Something went wrong.')
        
    return redirect('ecommerce:home')


def delete(request):
    ...