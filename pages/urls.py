from django.urls import path
from .views import client

urlpatterns = [
    path('Clients/', client, name='Clients'),
]
