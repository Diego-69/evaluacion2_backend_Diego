"""
Modelos de la aplicación de ventas.
Incluye: Cliente, Producto, Venta y DetalleVenta
"""
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Cliente(models.Model):
    """
    Modelo para almacenar información de clientes.
    """
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Email")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.TextField(verbose_name="Dirección")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"
    
    @property
    def nombre_completo(self):
        """Retorna el nombre completo del cliente."""
        return f"{self.nombre} {self.apellido}"


class Producto(models.Model):
    """
    Modelo para almacenar información de productos.
    """
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio"
    )
    stock = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)],
        verbose_name="Stock"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Venta(models.Model):
    """
    Modelo para almacenar información de ventas.
    """
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        related_name='ventas',
        verbose_name="Cliente"
    )
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Venta")
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        verbose_name="Total"
    )
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta']
    
    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre_completo} - ${self.total}"
    
    def calcular_total(self):
        """
        Calcula el total de la venta sumando todos los detalles.
        """
        total = sum(detalle.subtotal for detalle in self.detalles.all())
        self.total = total
        self.save()
        return total


class DetalleVenta(models.Model):
    """
    Modelo para almacenar los detalles de cada venta.
    Relación muchos a muchos entre Venta y Producto.
    """
    venta = models.ForeignKey(
        Venta, 
        on_delete=models.CASCADE, 
        related_name='detalles',
        verbose_name="Venta"
    )
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        related_name='ventas',
        verbose_name="Producto"
    )
    cantidad = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Cantidad"
    )
    precio_unitario = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Precio Unitario"
    )
    subtotal = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Subtotal"
    )
    
    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"
        ordering = ['venta', 'producto']
    
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} - ${self.subtotal}"
    
    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para calcular automáticamente el subtotal.
        """
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
        # Actualizar el total de la venta
        self.venta.calcular_total()
