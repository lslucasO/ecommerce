from django import forms
from ecommerce.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'stock',   
            'cover',
            'category'             
        ]
    