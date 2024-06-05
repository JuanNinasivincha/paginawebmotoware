from django.shortcuts import render

def login_view(request):
    return render(request, 'nosotros/login.html')


def crear_cuenta(request):
    return render(request, 'nosotros/create.html')