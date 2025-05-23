from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

from . import models
from .models import Product, ProductComment
from .forms import ProductCommentForm
# from cart.forms import AddToCartProductForm

class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True) #show evrithing in model if active filds is true
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    # def get(request):
    #     messages.success(request, "welcome to product page!")
    #     return render(request, 'products/product_list.html')

    # model = models.Product  --- show all of things saved in model
    # success_message = "Wellcome to product's part" #this messages use for actual method like delete or create and etc
    # success_url = reverse_lazy('product_list')

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ProductCommentForm()
        # context['add_to_cart_form'] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView, SuccessMessageMixin):
    model = ProductComment
    form_class = ProductCommentForm

    # def get_success_url(self):
    #     return reverse('product_list',)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        messages.success(self.request, _('Comment Successfully Created'))

        return super().form_valid(form)

