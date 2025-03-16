from django.urls import include, path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('users/', views.dashboard_users, name='users'),
    path('products/', views.dashboard_products, name='products'),
    path('reviews/', views.dashboard_reviews, name='reviews'),
    path('product_edit_view/<int:id>', views.dashboard_product_edit_view, name='product_edit_view'),
    path('product_edit_create/<int:id>', views.dashboard_product_edit_create, name='product_edit_create'),
    path('product_create_view/', views.dashboard_product_create_view, name='product_create_view'),
    path('product_create_submit/', views.dashboard_product_create_submit, name='product_create_submit'),
    path('product_delete/', views.dashboard_product_delete, name='product_delete'),
] 
