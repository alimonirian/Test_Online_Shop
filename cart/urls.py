from django.urls import (path, include)

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart_view, name='cart_add'),
    path('remove/<int:product_id>/', views.remove_from_cart_view, name='cart_remove'),
    path('clear/', views.clear_cart_view, name='cart_clear'),
]
