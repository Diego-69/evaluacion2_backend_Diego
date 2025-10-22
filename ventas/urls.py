"""
Configuración de URLs para la aplicación de ventas.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # URLs de Clientes
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.cliente_delete, name='cliente_delete'),
    
    # URLs de Productos
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/crear/', views.producto_create, name='producto_create'),
    path('productos/<int:pk>/editar/', views.producto_update, name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
    
    # URLs de Ventas
    path('ventas/', views.venta_list, name='venta_list'),
    path('ventas/crear/', views.venta_create, name='venta_create'),
    path('ventas/<int:pk>/agregar-productos/', views.venta_add_productos, name='venta_add_productos'),
    path('ventas/<int:pk>/detalle/', views.venta_detail, name='venta_detail'),
    path('ventas/<int:pk>/eliminar/', views.venta_delete, name='venta_delete'),
    path('ventas/detalle/<int:pk>/eliminar/', views.venta_detalle_delete, name='venta_detalle_delete'),
]
