"""
Serializers para la API REST de Ventas.
Convierten los modelos de Django a formato JSON y viceversa.
"""
from rest_framework import serializers
from .models import Cliente, Producto, Venta, DetalleVenta
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo User de Django.
    Utilizado para mostrar información del usuario autenticado.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Cliente.
    Incluye todos los campos del modelo y campos calculados.
    """
    nombre_completo = serializers.ReadOnlyField()
    total_ventas = serializers.SerializerMethodField()
    
    class Meta:
        model = Cliente
        fields = [
            'id',
            'rut',
            'nombre',
            'apellido',
            'nombre_completo',
            'email',
            'telefono',
            'direccion',
            'fecha_registro',
            'total_ventas'
        ]
        read_only_fields = ['id', 'fecha_registro']
    
    def get_total_ventas(self, obj):
        """Retorna el número total de ventas del cliente."""
        return obj.ventas.count()
    
    def validate_rut(self, value):
        """Validación personalizada para el RUT."""
        if not value:
            raise serializers.ValidationError("El RUT es obligatorio.")
        return value.upper()


class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Producto.
    Incluye validaciones personalizadas para precio y stock.
    """
    disponible = serializers.SerializerMethodField()
    
    class Meta:
        model = Producto
        fields = [
            'id',
            'codigo',
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'disponible',
            'fecha_creacion',
            'fecha_actualizacion'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']
    
    def get_disponible(self, obj):
        """Indica si el producto tiene stock disponible."""
        return obj.stock > 0
    
    def validate_precio(self, value):
        """Validación para el precio."""
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value
    
    def validate_stock(self, value):
        """Validación para el stock."""
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value


class DetalleVentaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo DetalleVenta.
    Incluye información del producto asociado.
    """
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_codigo = serializers.CharField(source='producto.codigo', read_only=True)
    
    class Meta:
        model = DetalleVenta
        fields = [
            'id',
            'producto',
            'producto_nombre',
            'producto_codigo',
            'cantidad',
            'precio_unitario',
            'subtotal'
        ]
        read_only_fields = ['id', 'subtotal']
    
    def validate_cantidad(self, value):
        """Validación para la cantidad."""
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a 0.")
        return value
    
    def validate(self, data):
        """
        Validación a nivel de objeto.
        Verifica que haya stock suficiente del producto.
        """
        producto = data.get('producto')
        cantidad = data.get('cantidad')
        
        if producto and cantidad:
            if producto.stock < cantidad:
                raise serializers.ValidationError(
                    f"Stock insuficiente. Disponible: {producto.stock}"
                )
        
        return data


class VentaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Venta.
    Incluye los detalles de la venta anidados.
    """
    detalles = DetalleVentaSerializer(many=True, read_only=True)
    cliente_nombre = serializers.CharField(source='cliente.nombre_completo', read_only=True)
    cantidad_productos = serializers.SerializerMethodField()
    
    class Meta:
        model = Venta
        fields = [
            'id',
            'cliente',
            'cliente_nombre',
            'fecha_venta',
            'total',
            'observaciones',
            'detalles',
            'cantidad_productos'
        ]
        read_only_fields = ['id', 'fecha_venta', 'total']
    
    def get_cantidad_productos(self, obj):
        """Retorna la cantidad total de productos en la venta."""
        return obj.detalles.count()


class VentaCreateSerializer(serializers.ModelSerializer):
    """
    Serializer especializado para la creación de ventas.
    Permite crear una venta con sus detalles en una sola petición.
    """
    detalles = DetalleVentaSerializer(many=True)
    
    class Meta:
        model = Venta
        fields = ['id', 'cliente', 'observaciones', 'detalles', 'total', 'fecha_venta']
        read_only_fields = ['id', 'total', 'fecha_venta']
    
    def create(self, validated_data):
        """
        Crea una venta con sus detalles de forma transaccional.
        """
        detalles_data = validated_data.pop('detalles')
        venta = Venta.objects.create(**validated_data)
        
        for detalle_data in detalles_data:
            producto = detalle_data['producto']
            cantidad = detalle_data['cantidad']
            
            # Verificar stock
            if producto.stock < cantidad:
                raise serializers.ValidationError(
                    f"Stock insuficiente para {producto.nombre}. Disponible: {producto.stock}"
                )
            
            # Crear detalle
            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio
            )
            
            # Actualizar stock
            producto.stock -= cantidad
            producto.save()
        
        # Calcular total
        venta.calcular_total()
        
        return venta


class VentaListSerializer(serializers.ModelSerializer):
    """
    Serializer simplificado para listar ventas.
    Incluye menos información para optimizar la respuesta.
    """
    cliente_nombre = serializers.CharField(source='cliente.nombre_completo', read_only=True)
    cantidad_productos = serializers.SerializerMethodField()
    
    class Meta:
        model = Venta
        fields = [
            'id',
            'cliente',
            'cliente_nombre',
            'fecha_venta',
            'total',
            'cantidad_productos'
        ]
        read_only_fields = fields
    
    def get_cantidad_productos(self, obj):
        """Retorna la cantidad total de productos en la venta."""
        return obj.detalles.count()
