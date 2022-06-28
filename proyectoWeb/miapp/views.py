from msilib.schema import ListView
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from miapp.models import Producto, TipoProducto
from .forms import ContactForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductoSerializer
from django.views.generic import ListView
from django.db.models import Q

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
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
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

@permission_required('miapp.add_producto')
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

@permission_required('miapp.view_producto')
def listarProductos(request):

    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }


    return render(request, 'app/tools/listar.html', data)

@permission_required('miapp.change_producto')
def modificarProducto(request, id):
    
    producto = get_object_or_404(Producto, id_producto=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to='listar_productos')
        data['form'] = formulario

    return render(request, 'app/tools/modificar.html', data)

@permission_required('miapp.delete_producto')
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    producto.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to='listar_productos')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            dj_login(request, user)
            return redirect(to='index')
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)


def adopta(request):
    return render(request, 'app/adopta.html')


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        return productos

#Filtro para el botón de busqueda
class SearchResults(ListView):
    model = Producto
    template_name = 'app/products.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Producto.objects.filter(
            Q(nombre__icontains=query)
        )
        return object_list