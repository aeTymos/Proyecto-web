from django.contrib import admin
from .models import Contacto, Region, Ciudad, Comuna, Usuario, Pedido, DetallePedido, Producto, TipoProducto

#Register your models here.
class productoAdmin(admin.ModelAdmin):
    list_per_page: 8

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Usuario)    
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Producto, productoAdmin)
admin.site.register(TipoProducto)
admin.site.register(Contacto)