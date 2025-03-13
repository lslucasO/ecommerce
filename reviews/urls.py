from django.urls import include, path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.create, name='create'),
] 
