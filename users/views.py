from django.shortcuts import render
from users.forms import LoginForm, RegisterForm


def register_view(request):
    form = RegisterForm()
    
    return render(request, 'users/pages/register.html', {
        'title': 'Register',
        'form': form,
    })


def login_view(request):
    form = LoginForm()
    
    return render(request, 'users/pages/login.html', {
        'title': 'Login',
        'form': form,
    })

