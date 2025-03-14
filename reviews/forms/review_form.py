from django import forms
from reviews.models import Review
from utils.django_forms import add_placeholder


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'topic',
            'text',
            'rating',             
        ]
    
    choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    rating = forms.ChoiceField(
        choices=choices,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )