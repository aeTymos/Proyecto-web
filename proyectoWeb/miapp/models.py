# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField()
    completado = models.BooleanField(default=False)
    id_transaccion = models.CharField(max_length=50, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.id_pedido


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    sku = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_agregado = models.DateField()
    miniatura = models.ImageField(upload_to='products', null=True)
    tipo_de_producto = models.ForeignKey('TipoProducto', models.CASCADE, db_column='tipo_producto.id_tiproducto')


    def __str__(self):
        return self.nombre


class PedidoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado = models.DateField()


class TipoProducto(models.Model):
    id_tiproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre


class DireccionEnvio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    direccion = models.CharField(max_length=100, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    comuna = models.CharField(max_length=50, null=False)
    codigo_postal = models.CharField(max_length=10, null=False)
    fecha_agregado = models.DateField()

    def __str__(self):
        return self.direccion

opcionesConsultas = [
    [0, 'Consulta'],
    [1, 'Reclamo'],
    [2, 'Sugerencia']
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()
    tipo_Consulta = models.IntegerField(choices=opcionesConsultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre