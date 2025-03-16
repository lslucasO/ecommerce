
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
        'form_action': reverse('dashboard:product_edit_create', args=[product.id])
    })
    
    
@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_product_edit_create(request, id):
    if not request.POST:
        raise Http404()
    
    
    product = get_object_or_404(
        Product,
        pk=id,
    )
    
    form = ProductForm(request.POST, instance=product)

    
    if form.is_valid():
        form.save()
        
        messages.success(request, 'Your product was edited with success.')
    else:
        messages.error(request, 'Something went wrong')
    
    return redirect(reverse('dashboard:products'))


@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_product_create_view(request):
    form = ProductForm()
    
    return render(request, 'dashboard/pages/dashboard-product-create-view.html', {
        'title': 'Dashboard | New Product',
        'form': form,
        'form_action': reverse('dashboard:product_create_submit')
    })
    
    
@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_product_create_submit(request):
    if not request.POST:
        raise Http404()
    
    form = ProductForm(request.POST, request.FILES)
    
    if form.is_valid():
        form.save()
        
        messages.success(request, 'Your product was edited with success.')
    else:
        messages.error(request, 'Something went wrong')
    
    return redirect(reverse('dashboard:products'))


@login_required(login_url='users:login', redirect_field_name='next')
def dashboard_product_delete(request):
    if not request.POST:
        raise Http404()
    
    product_id = request.POST.get('product_id')
    
    product = get_object_or_404(
        Product,
        pk=product_id
    )
    
    product.delete()
    
    messages.success(request, 'Your product was deleted with success.')
    
    return redirect(reverse('dashboard:products'))