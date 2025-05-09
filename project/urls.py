from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('reviews/', include('reviews.urls')),
    path('dashboard/', include('dashboard.urls'))
]
