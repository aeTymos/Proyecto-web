from django.http import HttpResponse
from django.shortcuts import render
from miapp.models import Producto

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def products(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/products.html', data)

def suscripcion(request):
    return render(request, 'app/suscripcion.html')

def login(request):
    return render(request, 'app/login.html')

def error(request):
    return render(request, 'app/error.html')

def cart(request):
    return render(request, 'app/cart.html')