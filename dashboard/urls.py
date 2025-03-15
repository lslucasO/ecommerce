from django.urls import include, path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('users/', views.dashboard_users, name='users'),
    path('products/', views.dashboard_products, name='products'),
] 
