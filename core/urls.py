from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('shop.urls')),
    path('', include('shopdetail.urls')),
    path('', include('pages.urls')),
    path('', include('users.urls')),
    path('', include('contact.urls')),
]
