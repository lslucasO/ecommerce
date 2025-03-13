from django.urls import include, path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_summary, name='cart'),
] 
