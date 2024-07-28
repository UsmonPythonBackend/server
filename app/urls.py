from django.urls import path
from app .views import home_view, shop, shop_detail, products, product_detail
from users .views import cart, xaridlar, users, xatolik
from contact .views import contact
urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', shop, name='shop'),
    path('shop_detail/', shop_detail, name='shop_detail'),
    path('cart/', cart, name='cart'),
    path('xaridlar/', xaridlar, name='xaridlar'),
    path('users/', users, name='users'),
    path('xatolik/', xatolik, name='xatolik'),
    path('contact/', contact, name='contact'),
    path('product/', products, name='products'),
    path('products/<slug:slug>/', product_detail, name='product-detail'),
]
