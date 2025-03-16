
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from ecommerce.forms import ProductForm
from ecommerce.models import Product
from reviews.models import Review

    
@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_users(request):
    users = User.objects.all().order_by('-date_joined')
    
    
    return render(request, 'dashboard/pages/dashboard-users.html', {
        'title': 'Dashboard',
        'users': users,
    })
    
    
@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_products(request):
    products = Product.objects.all().order_by('-id')
    
    
    return render(request, 'dashboard/pages/dashboard-products.html', {
        'title': 'Dashboard',
        'products': products,
    })
    
@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_reviews(request):
    reviews = Review.objects.all().order_by('-id')
    
    
    return render(request, 'dashboard/pages/dashboard-reviews.html', {
        'title': 'Dashboard',
        'reviews': reviews,
    })
    
@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_product_edit_view(request, id):
    
    product = get_object_or_404(
        Product,
        pk=id
    )
    
    form = ProductForm(instance=product)
    
    return render(request, 'dashboard/pages/dashboard-product-edit.html', {
        'title': 'Dashboard | Edit Product',
        'form': form,
        'form_action': reverse('dashboard:edit_create', args=[product.id])
    })
    

    
@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_product_edit_create(request, id):
    if not request.POST:
        raise Http404()
    
    
    product = get_object_or_404(
        Product,
        pk=id,
        stock=True
    )
    
    form = ProductForm(request.POST, instance=product)

    print(f"ID do produto antes de salvar: {product.id}")  # Verifique o ID antes de salvar
    
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        
        print(f"ID do produto após salvar: {product.id}")  # Verifique o ID após salvar
        
        messages.success(request, 'Your product was edited with success.')
    else:
        messages.error(request, 'Something went wrong')
    
    return redirect(reverse('dashboard:products'))