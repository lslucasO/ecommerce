from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from reviews.models import Review
from .forms import ReviewForm
from django.contrib import messages
from ecommerce.models import Product  # Import the Product model
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login', redirect_field_name='next')
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


@login_required(login_url='users:login', redirect_field_name='next')
def delete(request):
    if not request.POST:
        raise Http404()
    
    review_id = request.POST.get('review_id')
    
    
    review = get_object_or_404(
        Review,
        pk=review_id
    )
    
    review.delete()
    
    messages.success(request, 'Your review was deleted.')
    
    return redirect('ecommerce:home')


@login_required(login_url='users:login', redirect_field_name='next')
def edit(request):
    if not request.POST:
        raise Http404()
    
    
    review_id = request.POST.get('review_id')
    
    review = get_object_or_404(
        Review,
        pk=review_id
    )
    
    form = ReviewForm(request.POST, instance=review)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, 'Your review was edited.')
    else:
        messages.error(request, 'Something went wrong.')
            
    return redirect('ecommerce:home')
