from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import LoginForm, RegisterForm
from django.contrib import messages

from users.models import Account


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    
    return render(request, 'users/pages/register.html', {
        'title': 'Register',
        'form': form,
        'form_action': reverse('users:register_create')
    })


def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    FILES = request.FILES
    
    request.session['register_form_data'] = POST
    form = RegisterForm(POST, FILES)
    
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        
        # Handle the profile image separately
        profile_img = form.cleaned_data.get('profile_img')
        if profile_img:
            account = Account(account=user, profile_img=profile_img)
            account.save()
        
        messages.success(request, 'Account created, please log in')
        
        del(request.session['register_form_data'])
        return redirect(reverse('users:login'))
    
    print('inválido')
    return redirect('users:register')
        
        
def login_view(request):
    form = LoginForm()
    
    return render(request, 'users/pages/login.html', {
        'title': 'Login',
        'form': form,
    })

