from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Cart:
    def __init__(self, request):
        """
        add a product to cart
        :param request:
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}
            # cart = self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1, replace_current_quantity = False):
        """
        add a product to cart
        :param product:
        :param quantity:
        :return:
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, _('Product has been added to cart'))

        self.save()

    def remove(self, product):
        """
        remove a product from cart
        :param product:
        :return:
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('Product has been deleted from cart'))
            self.save()

    def save(self):
        """
        save the cart
        :return:
        """
        self.session.modified = True

    def __iter__(self):
        """
        iterate the cart
        :return:
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price']= item['product_obj'].price * item['quantity']
            yield item

    def __len__(self):
        # return len(self.cart.keys()) # return count of product kind
        return sum(item['quantity'] for item in self.cart.values()) # return sum of choicess product to cart


    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())


    def is_empty(self):
        if self.cart:
            return False
        return True


