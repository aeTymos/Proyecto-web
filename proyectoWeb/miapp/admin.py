from django.contrib import admin
from .models import Region, Ciudad, Comuna, Usuario, Pedido, DetallePedido, Producto, TipoProducto

# Register your models here.
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Producto)
admin.site.register(TipoProducto)