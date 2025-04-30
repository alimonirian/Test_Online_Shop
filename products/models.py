from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone



class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Product Title'))
    description = models.TextField(verbose_name=_('Product Description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Product Price'))
    active = models.BooleanField(default=True, verbose_name=_('Product Active'))
    image = models.ImageField(upload_to='products/product_image', verbose_name=_('Product Image'), blank=True,)

    # datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Product Created'))  #when time created auto add
    datetime_created = models.DateTimeField(default= timezone.now, verbose_name=_('Product Created')) #to show datepicker on admin panel
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Product Modified'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])

#custom_manager
# class ActiveCommentsManager(models.Manager):
#     def get_queryset(self):
#         return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class ProductComment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Very Good')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                               verbose_name=_('Comment Author'))
    body = models.TextField(verbose_name=_('Comment Text'))
    datetime_created = models.DateTimeField(auto_now_add=True,verbose_name=_('Date Created'))
    datetime_modified = models.DateTimeField(auto_now=True,verbose_name=_('Date Modified'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('Comment Stars'))
    active = models.BooleanField(default=True,verbose_name=_('Comment Active'))

    #use_custom_manager
    # objects = models.Manager()
    # active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])


