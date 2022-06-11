# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms import CharField, EmailField, IntegerField


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=40)
    region_id_region = models.ForeignKey('Region', models.CASCADE, db_column='region_id_region')

    def __str__(self):
        return self.nombre_ciudad


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=40)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.CASCADE, db_column='ciudad_id_ciudad')
    
    def __str__(self):
        return self.nombre_comuna


class DetallePedido(models.Model):
    costo_pedido = models.IntegerField()
    cantidad = models.IntegerField()
    producto_id_producto = models.ForeignKey('Producto', models.CASCADE, db_column='producto_id_producto')
    pedido_id_pedido = models.ForeignKey('Pedido', models.CASCADE, db_column='pedido_id_pedido')


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    direccion_envio = models.CharField(max_length=60)
    direccion_pedido = models.CharField(max_length=60)
    correo_pedido = models.CharField(max_length=50)
    fecha_pedido = models.DateField()
    estado_pedido = models.CharField(max_length=20)
    id_usuario = models.ForeignKey('Usuario', models.CASCADE, db_column='usuario_id_usuario', 
                         related_name='idUsuarioEnPedido')
    id_comuna = models.ForeignKey('Usuario', models.CASCADE, db_column='usuario_comuna_id_comuna', 
                               related_name='idComunaEnUsuario')
    
    def __str__(self):
        return self.id_pedido


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    sku = models.CharField(unique=True, max_length=12)
    nombre_producto = models.CharField(max_length=50)
    descrip_producto = models.CharField(max_length=200)
    precio_producto = models.IntegerField()
    stock_producto = models.CharField(max_length=40)
    fecha_agregado = models.DateField()
    miniatura = models.ImageField(upload_to='products', null=True)
    id_tiproducto = models.ForeignKey('TipoProducto', models.CASCADE, db_column='tipo_producto.id_tiproducto')


    def __str__(self):
        return self.nombre_producto


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre_region


class TipoProducto(models.Model):
    id_tiproducto = models.AutoField(primary_key=True)
    nombre_tiproducto = models.CharField(max_length=20)
    descrip_tiproducto = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre_tiproducto


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo_usuario = models.CharField(unique=True, max_length=50)
    nombre_usuario = models.CharField(unique=True, max_length=25)
    pass_usuario = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    dir_envio_default = models.CharField(max_length=60)
    fono_usuario = models.CharField(max_length=12)
    comuna_id_comuna = models.ForeignKey(Comuna, models.CASCADE, db_column='comuna_id_comuna')


    def __str__(self):
        return self.nombre_usuario

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