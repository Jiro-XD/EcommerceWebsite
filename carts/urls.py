from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('reduce_cart/<int:product_id>/<int:cart_item_id>/', views.reduce_cart, name='reduce_cart'),
    path('remove_cartItem/<int:product_id>/<int:cart_item_id>/', views.remove_cartItem, name='remove_cartItem'),

    path('checkout/', views.checkout, name='checkout'),
]
