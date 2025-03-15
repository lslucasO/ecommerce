from django.urls import include, path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('users/', views.dashboard_users, name='users'),
    path('products/', views.dashboard_products, name='products'),
    path('reviews/', views.dashboard_reviews, name='reviews'),
    path('edit/<int:id>', views.dashboard_product_edit_view, name='edit_view'),
    path('create/<int:id>', views.dashboard_product_edit_create, name='edit_create'),
] 
