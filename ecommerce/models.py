from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=165)
    price = models.FloatField()
    description = models.TextField(max_length=600)
    stock = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    cover = models.ImageField(
        upload_to='ecommerce/covers/%Y/%m/%d/', blank=True, default=''
    )
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )
    
    def __str__(self):
        return self.name