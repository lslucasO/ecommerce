from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf import settings

from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)