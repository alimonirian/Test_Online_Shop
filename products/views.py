from django.views import generic
from django.shortcuts import get_object_or_404,reverse

# from . import models
from .models import Product,ProductComment
from .forms import ProductCommentForm


class ProductListView(generic.ListView):
    # model = models.Product  --- show all of things saved in model
    queryset = Product.objects.filter(active=True) #show evrithing in model if active filds is true
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ProductCommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = ProductComment
    form_class = ProductCommentForm

    # def get_success_url(self):
    #     return reverse('product_list',)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id= product_id)
        obj.product = product

        return super().form_valid(form)