from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    prepopulated_fields = {
        "slug": ('name',)
    }

class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)