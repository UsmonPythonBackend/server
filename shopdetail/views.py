from django.shortcuts import render


def shop_detail(request):
    return render(request, 'product.html')
