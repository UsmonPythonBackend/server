from django.shortcuts import render


def client(request):
    return render(request, 'xaridlar.html')
