from django.shortcuts import render


def home(request):
    return render(request, 'ecommerce/pages/home.html', {
        'page_title': 'Home'
    })
