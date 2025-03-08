from django.shortcuts import render
from users.forms import LoginForm


def login_view(request):
    form = LoginForm()
    
    return render(request, 'users/pages/login.html', {
        'title': 'Login',
        'form': form,
    })
