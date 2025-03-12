from django.urls import include, path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_summary, name='cart'),
    path('add/', views.cart_add, name='cart_add'),
    path('update/', views.cart_update, name='cart_update')
] 
