from .models import Producto, TipoProducto
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):

    #Para ordenar un poco el JSON
    nombre_categoria = serializers.CharField(read_only=True, source='tipo_de_producto.nombre')
    tipo_de_producto = CategoriaSerializer(read_only=True)  
    id_tiproducto = serializers.PrimaryKeyRelatedField(queryset=TipoProducto.objects.all(), source='tipo_de_producto')
    
    #Validación dentro del formulario de la API
    sku = serializers.CharField(required=True, max_length=12)
    nombre = serializers.CharField(required=True, min_length=3)

    def validaNombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()
        if existe:
            raise serializers.ValidationError('Ya existe un producto con este nombre')

        return value
        
    class Meta:
        model = Producto
        fields = '__all__'