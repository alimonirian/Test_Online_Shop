from django.views import generic

from . import models
# from .models import Product
class ProductListView(generic.ListView):
    # model = models.Product  --- show all of things saved in model
    queryset = models.Product.objects.filter(active=True) #show evrithing in model if active filds is true
    template_name = 'products/product.list.html'
    context_object_name = 'products'
