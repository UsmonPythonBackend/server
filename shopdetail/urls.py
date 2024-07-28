from django.urls import path
from .views import shop_detail

urlpatterns = [
    path('shop_detail/', shop_detail, name='shop-detail'),
]
