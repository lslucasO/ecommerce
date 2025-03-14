from django.urls import include, path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
] 
