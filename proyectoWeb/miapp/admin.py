from django.contrib import admin
from .models import Contacto, Usuario, Pedido, DetallePedido, Producto, TipoProducto
from .forms import ProductoForm

#Register your models here.
class productoAdmin(admin.ModelAdmin):
    list_per_page: 8
    form = ProductoForm

admin.site.register(Usuario)    
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Producto, productoAdmin)
admin.site.register(TipoProducto)
admin.site.register(Contacto)