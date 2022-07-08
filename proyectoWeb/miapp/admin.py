from django.contrib import admin
from .models import Contacto, Usuario, Pedido, Producto, TipoProducto, PedidoProducto, DireccionEnvio
from .forms import ProductoForm

#Register your models here.
class productoAdmin(admin.ModelAdmin):
    list_per_page: 8
    form = ProductoForm

admin.site.register(Usuario)    
admin.site.register(Pedido)
admin.site.register(Producto, productoAdmin)
admin.site.register(TipoProducto)
admin.site.register(PedidoProducto)
admin.site.register(DireccionEnvio)
admin.site.register(Contacto)