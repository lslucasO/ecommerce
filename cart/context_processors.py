from .cart import Cart

# Creat context processor so cart work on all pages
def cart(request):
    return {'cart': Cart(request)}