from django.shortcuts import render
from shop.models import Product

def home_view(request):
    return render(request, 'index.html')


def shop(request):
    return render(request, 'shop.html')


def shop_detail(request):
    return render(request, 'product.html')


def xaridlar(request):
    return render(request, 'xaridlar.html')


def cart(request):
    return render(request, 'cart.html')


def users(request):
    return render(request, 'users.html')


def xatolik(request):
    return render(request, 'Xatolik.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def products(request):
    if request.method == 'POST':
        search = request.POST['search']
        products = Product.objects.filter(title__icontains=search)
        if products:
            return render(request, 'shop.html', {'products': products, 'value': search, "massage": 'Succesfully'})
        else:
            return render(request, 'shop.html', {"massage": 'not found'})
    product = Product.objects.all()
    return render(request, 'shop.html', {'products': product})


def product_detail(request, slug):
    product = Product.objacts.get(slug=slug)
    if product:
        return render(request, 'product.html', {'product': product, "message": 'Succesfully'})
    else:
        return render(request, 'product.html', {"message": 'Not found'})