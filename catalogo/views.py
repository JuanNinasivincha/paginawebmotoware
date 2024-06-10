from django.shortcuts import render


def index(request):
    return render(request, 'catalogo/index.html')

def categoria1(request):
    return render(request, 'catalogo/categoria1.html')

def categoria2(request):
    return render(request, 'catalogo/categoria2.html')

def categoria3(request):
    return render(request, 'catalogo/categoria3.html')

def categoria4(request):
    return render(request, 'catalogo/categoria4.html')

def categoria5(request):
    return render(request, 'catalogo/categoria5.html')

def categoria6(request):
    return render(request, 'catalogo/categoria6.html')

def otros(request):
    return render(request, 'catalogo/otros.html')

def aboutus(request):
    return render(request, 'catalogo/nosotros.html')

def busquedaavanzada(request):
    return render(request, 'catalogo/search.html')