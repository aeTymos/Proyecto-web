"""proyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import eliminarProducto, index, about, modificarProducto, products, actualizarProducto,suscripcion, login,\
     agregarProducto, listarProductos, registro, adopta, ProductoViewSet
from rest_framework import routers
#Solo en debug
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('suscripcion/', suscripcion, name='suscripcion'),
    path('products/', products, name='products'),
    path('actualiza-producto/', actualizarProducto, name='actualizar_producto'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('agregar-producto/', agregarProducto, name='agregar_producto'),
    path('listar-productos/', listarProductos, name='listar_productos'),
    path('modificar-producto/<id>/', modificarProducto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminarProducto, name='eliminar_producto'),
    path('registro/', registro, name='registro'),
    path('adopta/', adopta, name='adopta'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)