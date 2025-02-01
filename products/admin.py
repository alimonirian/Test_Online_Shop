from django.contrib import admin

from .models import Product, ProductComment


class ProductCommentsInline(admin.TabularInline):
    model = ProductComment
    fields = ['author', 'body', 'stars', 'active',]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [ProductCommentsInline]


@admin.register(ProductComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active',]
