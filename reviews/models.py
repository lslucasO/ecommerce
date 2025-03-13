from django.db import models
from django.contrib.auth.models import User
from ecommerce.models import Product

class Review(models.Model):
    topic = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )
    
    def __str__(self):
        return self.topic