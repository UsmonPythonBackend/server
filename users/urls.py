from django.urls import path
from .views import cart, xaridlar, users, xatolik, login_view, register_view, logout_view

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('xaridlar/', xaridlar, name='xaridlar'),
    path('users/', users, name='users'),
    path('xatolik/', xatolik, name='xatolik'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
