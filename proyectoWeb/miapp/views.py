from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from miapp.models import Producto
from .forms import ContactForm, ProductoForm

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

def agregarProducto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado correctamente'
        else:
            data['form'] = formulario

    return render(request, 'app/tools/agregar.html', data)

def listarProductos(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'app/tools/listar.html', data)

def modificarProducto(request, id):
    
    producto = get_object_or_404(Producto, id_producto=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_productos')
        else:
            data['form'] = formulario

    return render(request, 'app/tools/modificar.html', data)