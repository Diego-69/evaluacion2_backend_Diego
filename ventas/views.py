"""
Vistas de la aplicación de ventas.
Implementa CRUD para Cliente, Producto y Venta.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Count, F
from .models import Cliente, Producto, Venta, DetalleVenta
from .forms import ClienteForm, ProductoForm, VentaForm, DetalleVentaForm
import json


# ==================== VISTA HOME ====================
def home(view):
    """
    Vista principal que muestra los informes:
    - Productos más vendidos
    - Clientes con más ventas
    """
    # Productos más vendidos
    productos_mas_vendidos = (
        DetalleVenta.objects
        .values('producto__nombre')
        .annotate(total_vendido=Sum('cantidad'))
        .order_by('-total_vendido')[:10]
    )
    
    # Clientes con más ventas
    clientes_mas_ventas = (
        Venta.objects
        .values('cliente__nombre', 'cliente__apellido')
        .annotate(
            total_compras=Sum('total'),
            cantidad_ventas=Count('id')
        )
        .order_by('-total_compras')[:10]
    )
    
    # Preparar datos para gráficos
    productos_labels = [p['producto__nombre'] for p in productos_mas_vendidos]
    productos_data = [int(p['total_vendido']) for p in productos_mas_vendidos]
    
    clientes_labels = [
        f"{c['cliente__nombre']} {c['cliente__apellido']}" 
        for c in clientes_mas_ventas
    ]
    clientes_data = [float(c['total_compras']) for c in clientes_mas_ventas]
    
    context = {
        'productos_mas_vendidos': productos_mas_vendidos,
        'clientes_mas_ventas': clientes_mas_ventas,
        'productos_labels_json': json.dumps(productos_labels),
        'productos_data_json': json.dumps(productos_data),
        'clientes_labels_json': json.dumps(clientes_labels),
        'clientes_data_json': json.dumps(clientes_data),
    }
    
    return render(view, 'ventas/home.html', context)


# ==================== VISTAS CLIENTES ====================
def cliente_list(request):
    """Lista todos los clientes."""
    clientes = Cliente.objects.all()
    return render(request, 'ventas/cliente_list.html', {'clientes': clientes})


def cliente_create(request):
    """Crea un nuevo cliente."""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'ventas/cliente_form.html', {'form': form, 'action': 'Crear'})


def cliente_update(request, pk):
    """Actualiza un cliente existente."""
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente.')
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'ventas/cliente_form.html', {
        'form': form, 
        'action': 'Editar',
        'cliente': cliente
    })


def cliente_delete(request, pk):
    """Elimina un cliente."""
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('cliente_list')
    return render(request, 'ventas/cliente_confirm_delete.html', {'cliente': cliente})


# ==================== VISTAS PRODUCTOS ====================
def producto_list(request):
    """Lista todos los productos."""
    productos = Producto.objects.all()
    return render(request, 'ventas/producto_list.html', {'productos': productos})


def producto_create(request):
    """Crea un nuevo producto."""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'ventas/producto_form.html', {'form': form, 'action': 'Crear'})


def producto_update(request, pk):
    """Actualiza un producto existente."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ventas/producto_form.html', {
        'form': form, 
        'action': 'Editar',
        'producto': producto
    })


def producto_delete(request, pk):
    """Elimina un producto."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('producto_list')
    return render(request, 'ventas/producto_confirm_delete.html', {'producto': producto})


# ==================== VISTAS VENTAS ====================
def venta_list(request):
    """Lista todas las ventas."""
    ventas = Venta.objects.all().select_related('cliente')
    return render(request, 'ventas/venta_list.html', {'ventas': ventas})


def venta_create(request):
    """Crea una nueva venta."""
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            messages.success(request, 'Venta creada exitosamente. Ahora agregue productos.')
            return redirect('venta_add_productos', pk=venta.pk)
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_form.html', {'form': form, 'action': 'Crear'})


def venta_add_productos(request, pk):
    """Agrega productos a una venta existente."""
    venta = get_object_or_404(Venta, pk=pk)
    detalles = venta.detalles.all()
    
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.venta = venta
            detalle.precio_unitario = detalle.producto.precio
            
            # Verificar stock disponible
            if detalle.producto.stock >= detalle.cantidad:
                # Reducir stock
                detalle.producto.stock -= detalle.cantidad
                detalle.producto.save()
                
                # Guardar detalle
                detalle.save()
                messages.success(request, 'Producto agregado a la venta.')
                return redirect('venta_add_productos', pk=pk)
            else:
                messages.error(request, f'Stock insuficiente. Solo hay {detalle.producto.stock} unidades disponibles.')
    else:
        form = DetalleVentaForm()
    
    return render(request, 'ventas/venta_add_productos.html', {
        'form': form,
        'venta': venta,
        'detalles': detalles
    })


def venta_detalle_delete(request, pk):
    """Elimina un detalle de venta y restaura el stock."""
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    venta_pk = detalle.venta.pk
    
    # Restaurar stock
    detalle.producto.stock += detalle.cantidad
    detalle.producto.save()
    
    # Eliminar detalle
    detalle.delete()
    
    messages.success(request, 'Producto eliminado de la venta.')
    return redirect('venta_add_productos', pk=venta_pk)


def venta_detail(request, pk):
    """Muestra el detalle completo de una venta."""
    venta = get_object_or_404(Venta, pk=pk)
    detalles = venta.detalles.all()
    return render(request, 'ventas/venta_detail.html', {
        'venta': venta,
        'detalles': detalles
    })


def venta_delete(request, pk):
    """Elimina una venta completa y restaura el stock."""
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        # Restaurar stock de todos los productos
        for detalle in venta.detalles.all():
            detalle.producto.stock += detalle.cantidad
            detalle.producto.save()
        
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente.')
        return redirect('venta_list')
    return render(request, 'ventas/venta_confirm_delete.html', {'venta': venta})
