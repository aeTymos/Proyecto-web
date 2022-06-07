from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def suscripcion(request):
    return render(request, 'suscripcion.html')

def login(request):
    return render(request, 'login.html')

def error(request):
    return render(request, 'error.html')
    
def cart(request):
    return render(request, 'cart.html')