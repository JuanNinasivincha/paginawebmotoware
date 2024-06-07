from django.shortcuts import render

def quejas(request):
    return render(request, 'quejas/index.html')