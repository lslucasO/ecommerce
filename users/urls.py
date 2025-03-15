from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/create', views.login_create, name='login_create'),
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/<int:id>', views.profile, name='profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)