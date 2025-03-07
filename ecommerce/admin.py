from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    ...


class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)