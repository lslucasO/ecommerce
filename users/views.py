from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from reviews.forms.review_form import ReviewForm
from reviews.models import Review
from users.forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

from users.models import Account


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    
    return render(request, 'users/pages/register.html', {
        'title': 'Create Account',
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


    return redirect('users:register')
        
   
        
def login_view(request):
    form = LoginForm()
    
    return render(request, 'users/pages/login.html', {
        'title': 'Login',
        'form': form,
        'form_action': reverse('users:login_create')
    })



def login_create(request):
    form = LoginForm(request.POST)
    
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )
        
        if authenticated_user is not None:
            messages.success(request, 'Success, you are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')    
    else:
        messages.error(request, 'Invalid username or password')
        
    return redirect(reverse('ecommerce:home'))


@login_required(login_url='users:login', redirect_field_name='next')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out successfully')
    else:
        messages.error(request, 'You are not logged in')
    
    return redirect(reverse('ecommerce:home'))


@login_required(login_url='users:login', redirect_field_name='next')
def dashboard(request):
    
    return render(request, 'users/pages/dashboard.html', {
        'title': 'Dashboard'
    })
    

@login_required(login_url='users:login', redirect_field_name='next')
def profile(request, id):
    reviews = Review.objects.filter(
        user=id
    )
    
    # review_user_id = request.GET.get('review_user_id')
    # print(review_user_id)
    
    user = get_object_or_404(
        User,
        pk=id
    )
    
    form = ReviewForm()
    

    return render(request, 'users/pages/profile.html', {
        'title': 'Profile',
        'reviews': reviews,
        'form': form,
        'user': user,
    })