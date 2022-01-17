from decimal import Decimal
from django.conf import settings
# from shop.models import Product


class Cart(object):
    def __init__(self, request,value='cart'):
        self.value = value
        self.session = request.session
        cart = self.session.get(value)
        if not cart:
            cart = self.session[value] = {}
        self.cart = cart

    def add(self, product,price, quantity=1,total_price=0, update_quantity=False):

        total_price = f'{price * quantity:.2f}'
        # print(total_price)
        if product not in self.cart:
            self.cart[product] = {'quantity': 0, 'price': str(price)}
            self.cart[product]['total_price'] =total_price
        if update_quantity:
            self.cart[product]['quantity'] = quantity
            self.cart[product]['total_price'] =total_price
            # print("update_quantity",update_quantity)
        else:
            self.cart[product]['quantity'] += int(quantity)
            total_price ='{:.2f}'.format(self.cart[product]['quantity']*price)
            self.cart[product]['total_price'] =total_price
        self.save()

    def save(self):
        self.session[self.value ] = self.cart
        self.session.modified = True

        cart = self.session[self.value ]
        

        for k,v in cart.items():
            
            print('keys', k,'values', v)




    def remove(self, product):
        # product_id = str(product)
        if product in self.cart:
            del self.cart[product]
            self.save()
            print("cart",self.cart)

    def __iter__(self):
        product_ids = self.cart.keys()
        # products = Product.objects.filter(id__in=product_ids)
        for product in product_ids:
            self.cart[str(product)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        total_price = sum(Decimal(item['price']) * int(item['quantity']) for item in self.cart.values())
        total_price = '{:.2f}'.format(total_price)
        print(total_price)
        return total_price

    def clear(self):
        del self.session[self.value]
        self.session.modified = True
