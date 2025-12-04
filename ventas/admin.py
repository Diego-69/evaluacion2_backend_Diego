"""
Configuración del panel de administración de Django para los modelos de ventas.
"""
from django.contrib import admin
from .models import Cliente, Producto, Venta, DetalleVenta


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Configuración del admin para Cliente."""
    list_display = ['rut', 'nombre', 'apellido', 'email', 'telefono', 'fecha_registro']
    search_fields = ['rut', 'nombre', 'apellido', 'email']
    list_filter = ['fecha_registro']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Configuración del admin para Producto."""
    list_display = ['codigo', 'nombre', 'precio', 'stock', 'fecha_creacion']
    search_fields = ['codigo', 'nombre']
    list_filter = ['fecha_creacion']


class DetalleVentaInline(admin.TabularInline):
    """Inline para mostrar detalles de venta dentro de una venta."""
    model = DetalleVenta
    extra = 1
    readonly_fields = ['subtotal']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    """Configuración del admin para Venta."""
    list_display = ['id', 'cliente', 'fecha_venta', 'total']
    search_fields = ['cliente__nombre', 'cliente__apellido', 'cliente__rut']
    list_filter = ['fecha_venta']
    inlines = [DetalleVentaInline]
    readonly_fields = ['total']


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    """Configuración del admin para DetalleVenta."""
    list_display = ['venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    search_fields = ['venta__id', 'producto__nombre']
    readonly_fields = ['subtotal']
