from django.http import HttpResponse
from django.shortcuts import render
from miapp.models import Producto
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    data = {
        'form': ContactForm()
    }
    
    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto guardado'
        else:
            data['form'] = formulario

    return render(request, 'app/about.html', data)

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