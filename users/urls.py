from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)