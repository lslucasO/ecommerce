from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from ecommerce.models import Product

    
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