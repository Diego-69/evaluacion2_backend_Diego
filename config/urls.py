"""
Configuración de URLs del proyecto.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger/OpenAPI
schema_view = get_schema_view(
    openapi.Info(
        title="API de Gestión de Ventas",
        default_version='v1',
        description="""
        API RESTful para el Sistema de Gestión de Ventas.
        
        ## Características
        - Gestión completa de Clientes
        - Gestión completa de Productos
        - Gestión completa de Ventas
        - Autenticación mediante JWT (JSON Web Tokens)
        - Documentación interactiva con Swagger
        
        ## Autenticación
        Para usar la API, primero debes obtener un token JWT:
        1. Envía una petición POST a `/api/auth/login/` con username y password
        2. Usa el token recibido en el header `Authorization: Bearer <token>`
        
        ## Endpoints Principales
        - `/api/clientes/` - CRUD de clientes
        - `/api/productos/` - CRUD de productos
        - `/api/ventas/` - CRUD de ventas
        - `/api/auth/login/` - Obtener token JWT
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@ventas.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin de Django
    path('admin/', admin.site.urls),
    
    # URLs de la aplicación web (vistas tradicionales)
    path('', include('ventas.urls')),
    
    # URLs de la API REST
    path('api/', include('ventas.api_urls')),
    
    # Documentación de la API con Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', 
            schema_view.without_ui(cache_timeout=0), 
            name='schema-json'),
    path('swagger/', 
         schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
    path('redoc/', 
         schema_view.with_ui('redoc', cache_timeout=0), 
         name='schema-redoc'),
    
    # Navegador de API de Django REST Framework
    path('api-auth/', include('rest_framework.urls')),
]
