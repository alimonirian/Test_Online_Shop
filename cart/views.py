from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse, reverse_lazy


from products.models import Product
from .cart import Cart
from .forms import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={'quantity': item['quantity'],
                                                                             'inplace': True, })
    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
    })


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity= cleaned_data['inplace'])

        # messages.success(request, 'Your cart has been updated')

    return redirect('products:product_list')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect('cart:cart_detail')


@require_POST
def clear_cart_view(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, _('Cart cleared'))
    else:
        messages.error(request, _('Your cart is already empty'))

    return redirect('products:product_list')

