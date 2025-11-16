from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart_items/', views.cart_items, name='cart_items'),
    path('remove_cart_item/<int:id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/<int:id>/', views.cart, name='cart'),
    path('reels/', views.reels, name='reels'),
]

