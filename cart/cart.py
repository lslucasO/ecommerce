from ecommerce.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        
        # Get the current session key if it exists
        cart = self.session.get('session_key')
       
        # If the user is new, no sessino key, create one
        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}
        
        self.cart = cart
        
             
    def add(self, product):
        product_id = str(product.id)
        print(product_id)
        
        if product_id in self.cart:
            
            print('Não estou adicionando nada')
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            
        self.session.modified = True
    
    
    def get_products(self):
        # Get products with ids
        product_ids = self.cart.keys()
        
        # Filter
        products = Product.objects.filter(
            id__in = product_ids
        )
        
        return products
    
    def __len__(self):
        return len(self.cart)
