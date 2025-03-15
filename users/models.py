from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    
    profile_img = models.ImageField(
        upload_to='ecommerce/profile/%Y/%m/%d/', blank=True, default=''
    )