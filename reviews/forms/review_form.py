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
    