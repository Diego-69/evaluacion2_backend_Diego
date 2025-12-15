"""
ViewSets para la API REST de Ventas.
Proporciona endpoints CRUD completos para cada modelo.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Cliente, Producto, Venta, DetalleVenta
from .serializers import (
    UserSerializer,
    ClienteSerializer,
    ProductoSerializer,
    VentaSerializer,
    VentaCreateSerializer,
    VentaListSerializer,
    DetalleVentaSerializer
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para usuarios.
    Solo permite listar y ver detalles (lectura).
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """
        Endpoint personalizado para obtener información del usuario actual.
        GET /api/users/me/
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Clientes.
    Proporciona operaciones CRUD completas: list, create, retrieve, update, destroy.
    
    Endpoints:
    - GET    /api/clientes/          -> Listar todos los clientes
    - POST   /api/clientes/          -> Crear nuevo cliente
    - GET    /api/clientes/{id}/     -> Ver detalle de un cliente
    - PUT    /api/clientes/{id}/     -> Actualizar cliente completo
    - PATCH  /api/clientes/{id}/     -> Actualizar cliente parcial
    - DELETE /api/clientes/{id}/     -> Eliminar cliente
    - GET    /api/clientes/{id}/ventas/ -> Ver ventas de un cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    
    # Filtros de búsqueda
    search_fields = ['nombre', 'apellido', 'rut', 'email']
    ordering_fields = ['nombre', 'apellido', 'fecha_registro']
    ordering = ['-fecha_registro']
    
    @action(detail=True, methods=['get'])
    def ventas(self, request, pk=None):
        """
        Endpoint personalizado para obtener todas las ventas de un cliente.
        GET /api/clientes/{id}/ventas/
        """
        cliente = self.get_object()
        ventas = cliente.ventas.all()
        serializer = VentaListSerializer(ventas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def buscar_por_rut(self, request):
        """
        Endpoint para buscar cliente por RUT.
        GET /api/clientes/buscar_por_rut/?rut=12345678-9
        """
        rut = request.query_params.get('rut', None)
        if not rut:
            return Response(
                {'error': 'Debe proporcionar un RUT'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            cliente = Cliente.objects.get(rut=rut)
            serializer = self.get_serializer(cliente)
            return Response(serializer.data)
        except Cliente.DoesNotExist:
            return Response(
                {'error': 'Cliente no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )


class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Productos.
    Proporciona operaciones CRUD completas.
    
    Endpoints:
    - GET    /api/productos/              -> Listar todos los productos
    - POST   /api/productos/              -> Crear nuevo producto
    - GET    /api/productos/{id}/         -> Ver detalle de un producto
    - PUT    /api/productos/{id}/         -> Actualizar producto completo
    - PATCH  /api/productos/{id}/         -> Actualizar producto parcial
    - DELETE /api/productos/{id}/         -> Eliminar producto
    - GET    /api/productos/sin_stock/    -> Productos sin stock
    - GET    /api/productos/bajo_stock/   -> Productos con stock bajo
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    
    # Filtros de búsqueda
    search_fields = ['nombre', 'codigo', 'descripcion']
    ordering_fields = ['nombre', 'precio', 'stock', 'fecha_creacion']
    ordering = ['nombre']
    
    @action(detail=False, methods=['get'])
    def sin_stock(self, request):
        """
        Endpoint para listar productos sin stock.
        GET /api/productos/sin_stock/
        """
        productos = self.queryset.filter(stock=0)
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def bajo_stock(self, request):
        """
        Endpoint para listar productos con stock bajo (menor a 10).
        GET /api/productos/bajo_stock/?limite=10
        """
        limite = int(request.query_params.get('limite', 10))
        productos = self.queryset.filter(stock__lte=limite, stock__gt=0)
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def agregar_stock(self, request, pk=None):
        """
        Endpoint para agregar stock a un producto.
        POST /api/productos/{id}/agregar_stock/
        Body: {"cantidad": 10}
        """
        producto = self.get_object()
        cantidad = request.data.get('cantidad', 0)
        
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                return Response(
                    {'error': 'La cantidad debe ser mayor a 0'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            producto.stock += cantidad
            producto.save()
            
            serializer = self.get_serializer(producto)
            return Response({
                'message': f'Se agregaron {cantidad} unidades al stock',
                'producto': serializer.data
            })
        except ValueError:
            return Response(
                {'error': 'Cantidad inválida'},
                status=status.HTTP_400_BAD_REQUEST
            )


class VentaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Ventas.
    Proporciona operaciones CRUD completas con lógica especial para crear ventas.
    
    Endpoints:
    - GET    /api/ventas/              -> Listar todas las ventas
    - POST   /api/ventas/              -> Crear nueva venta
    - GET    /api/ventas/{id}/         -> Ver detalle de una venta
    - DELETE /api/ventas/{id}/         -> Eliminar venta
    - GET    /api/ventas/por_cliente/  -> Ventas filtradas por cliente
    - GET    /api/ventas/estadisticas/ -> Estadísticas de ventas
    """
    queryset = Venta.objects.all()
    permission_classes = [IsAuthenticated]
    
    # Filtros
    ordering_fields = ['fecha_venta', 'total']
    ordering = ['-fecha_venta']
    
    def get_serializer_class(self):
        """
        Retorna el serializer apropiado según la acción.
        """
        if self.action == 'create':
            return VentaCreateSerializer
        elif self.action == 'list':
            return VentaListSerializer
        return VentaSerializer
    
    @action(detail=False, methods=['get'])
    def por_cliente(self, request):
        """
        Endpoint para filtrar ventas por cliente.
        GET /api/ventas/por_cliente/?cliente_id=1
        """
        cliente_id = request.query_params.get('cliente_id', None)
        if not cliente_id:
            return Response(
                {'error': 'Debe proporcionar un cliente_id'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        ventas = self.queryset.filter(cliente_id=cliente_id)
        serializer = VentaListSerializer(ventas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        """
        Endpoint para obtener estadísticas generales de ventas.
        GET /api/ventas/estadisticas/
        """
        from django.db.models import Sum, Count, Avg
        
        stats = self.queryset.aggregate(
            total_ventas=Count('id'),
            monto_total=Sum('total'),
            promedio_venta=Avg('total')
        )
        
        return Response({
            'total_ventas': stats['total_ventas'] or 0,
            'monto_total': float(stats['monto_total'] or 0),
            'promedio_venta': float(stats['promedio_venta'] or 0)
        })
    
    def destroy(self, request, *args, **kwargs):
        """
        Sobrescribe el método destroy para devolver stock al eliminar venta.
        """
        venta = self.get_object()
        
        # Devolver stock de cada producto
        for detalle in venta.detalles.all():
            producto = detalle.producto
            producto.stock += detalle.cantidad
            producto.save()
        
        # Eliminar venta
        self.perform_destroy(venta)
        
        return Response(
            {'message': 'Venta eliminada y stock restaurado'},
            status=status.HTTP_204_NO_CONTENT
        )


class DetalleVentaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para DetalleVenta.
    Solo permite lectura (list, retrieve).
    Los detalles se crean automáticamente al crear una venta.
    
    Endpoints:
    - GET /api/detalles-venta/     -> Listar todos los detalles
    - GET /api/detalles-venta/{id}/ -> Ver detalle específico
    """
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    permission_classes = [IsAuthenticated]
    
    ordering = ['-venta__fecha_venta']
