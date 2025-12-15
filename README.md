# Sistema de Gestión de Ventas - Django + API REST

Sistema web completo de gestión de ventas desarrollado con Django, Tailwind CSS y API RESTful. Permite administrar clientes, productos, ventas mediante interfaz web tradicional y consumir datos vía API REST con autenticación JWT.

## 🚀 Características

### Interfaz Web
- ✅ **CRUD completo** para Clientes, Productos y Ventas
- 📊 **Dashboard con gráficos** de productos más vendidos y clientes con más compras
- 🎨 **Diseño moderno** con Tailwind CSS
- 💾 **Base de datos SQLite** para persistencia de datos
- 📱 **Responsive Design** - Compatible con dispositivos móviles
- 🔄 **Gestión automática de stock** - Se actualiza al realizar ventas
- 📈 **Gráficos interactivos** con Chart.js

### API RESTful
- 🔐 **Autenticación JWT** - Tokens seguros para acceso a la API
- 📡 **Endpoints REST completos** - CRUD para todos los modelos
- 📚 **Documentación Swagger** - Interfaz interactiva para probar la API
- 🔒 **Protección de rutas** - Autenticación requerida en endpoints sensibles
- 📤 **Respuestas JSON** - Formato estándar para integración
- 🎯 **Endpoints personalizados** - Estadísticas, búsquedas y acciones especiales

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Realizar migraciones de base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. (Opcional) Crear superusuario para el panel de administración

```bash
python manage.py createsuperuser
```

Siga las instrucciones para crear un usuario administrador.

### 4. (Opcional) Generar datos de prueba

Para probar la aplicación con datos de ejemplo:

```bash
python manage.py generar_datos_prueba
```

Este comando creará:
- 5 clientes de prueba
- 10 productos de ejemplo
- 20 ventas aleatorias con sus detalles

## ▶️ Ejecución

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Luego abra su navegador en: **http://127.0.0.1:8000/**

Para acceder al panel de administración de Django: **http://127.0.0.1:8000/admin/**

## 📱 Estructura del Proyecto

```
eva2_backend/
│
├── config/                  # Configuración del proyecto Django
│   ├── settings.py         # Configuraciones principales
│   ├── urls.py             # URLs principales
│   └── wsgi.py
│
├── ventas/                 # Aplicación principal
│   ├── models.py           # Modelos: Cliente, Producto, Venta, DetalleVenta
│   ├── views.py            # Vistas CRUD y Dashboard
│   ├── forms.py            # Formularios para cada modelo
│   ├── urls.py             # URLs de la aplicación
│   ├── admin.py            # Configuración del admin de Django
│   └── management/         # Comandos personalizados
│       └── commands/
│           └── generar_datos_prueba.py
│
├── templates/              # Plantillas HTML
│   ├── base.html          # Template base con Tailwind CSS
│   └── ventas/            # Templates específicos de ventas
│       ├── home.html
│       ├── cliente_*.html
│       ├── producto_*.html
│       └── venta_*.html
│
├── manage.py              # Script de gestión de Django
├── requirements.txt       # Dependencias del proyecto
└── db.sqlite3            # Base de datos SQLite (se crea automáticamente)
```

## 🎯 Funcionalidades

### 1. Dashboard (Home)
- Visualización de productos más vendidos con tabla y gráfico de barras
- Listado de clientes con más compras con tabla y gráfico circular
- Accesos rápidos a las funciones principales

### 2. Gestión de Clientes
- **Listar**: Ver todos los clientes registrados
- **Crear**: Agregar nuevos clientes con RUT, nombre, email, teléfono y dirección
- **Editar**: Modificar información de clientes existentes
- **Eliminar**: Eliminar clientes (se eliminan también sus ventas)

### 3. Gestión de Productos
- **Listar**: Ver inventario completo con código, nombre, precio y stock
- **Crear**: Agregar nuevos productos
- **Editar**: Actualizar información y stock de productos
- **Eliminar**: Eliminar productos del inventario
- **Indicadores de stock**: Colores según disponibilidad (verde/amarillo/rojo)

### 4. Gestión de Ventas
- **Listar**: Ver todas las ventas realizadas
- **Crear**: Proceso en 2 pasos:
  1. Seleccionar cliente y agregar observaciones
  2. Agregar productos con cantidades
- **Ver detalle**: Visualizar información completa de la venta
- **Eliminar**: Anular venta y restaurar stock automáticamente
- **Control de stock**: Solo permite vender productos con stock disponible

## 🎨 Tecnologías Utilizadas

- **Backend**: 
  - Django 4.2.7 - Framework web principal
  - Django REST Framework 3.16.1 - Framework para API REST
  - djangorestframework-simplejwt 5.5.1 - Autenticación JWT
  - drf-yasg 1.21.11 - Documentación Swagger/OpenAPI
- **Frontend**: 
  - Tailwind CSS (vía CDN) - Framework CSS
  - Chart.js - Biblioteca de gráficos
  - HTML5 y JavaScript
- **Base de Datos**: SQLite3
- **Iconos**: SVG (integrados)

## 📊 Modelos de Datos

### Cliente
- RUT (único)
- Nombre y Apellido
- Email
- Teléfono
- Dirección
- Fecha de registro

### Producto
- Código (único)
- Nombre
- Descripción
- Precio
- Stock
- Fechas de creación y actualización

### Venta
- Cliente (Foreign Key)
- Fecha de venta
- Total
- Observaciones

### DetalleVenta
- Venta (Foreign Key)
- Producto (Foreign Key)
- Cantidad
- Precio unitario
- Subtotal (calculado automáticamente)

## 🔐 Seguridad

- Protección CSRF en todos los formularios
- Validación de datos en modelos y formularios
- Prevención de inyección SQL mediante ORM de Django

## 🌐 API RESTful - Documentación

### Acceder a la Documentación Swagger

Una vez iniciado el servidor, acceda a:
- **Swagger UI**: http://127.0.0.1:8000/swagger/
- **ReDoc**: http://127.0.0.1:8000/redoc/
- **Navegador API**: http://127.0.0.1:8000/api/

### Autenticación con JWT

#### 1. Obtener Token de Acceso

**Endpoint**: `POST /api/auth/login/`

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "tu_usuario",
    "password": "tu_contraseña"
  }'
```

**Respuesta**:
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### 2. Usar el Token en las Peticiones

Incluya el token en el header `Authorization`:

```bash
curl -X GET http://127.0.0.1:8000/api/clientes/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

#### 3. Refrescar Token (cuando expire)

**Endpoint**: `POST /api/auth/refresh/`

```bash
curl -X POST http://127.0.0.1:8000/api/auth/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."}'
```

### Endpoints Principales de la API

#### 👥 Clientes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/clientes/` | Listar todos los clientes |
| POST | `/api/clientes/` | Crear nuevo cliente |
| GET | `/api/clientes/{id}/` | Obtener detalle de cliente |
| PUT | `/api/clientes/{id}/` | Actualizar cliente completo |
| PATCH | `/api/clientes/{id}/` | Actualizar cliente parcial |
| DELETE | `/api/clientes/{id}/` | Eliminar cliente |
| GET | `/api/clientes/{id}/ventas/` | Obtener ventas del cliente |
| GET | `/api/clientes/buscar_por_rut/?rut=12345678-9` | Buscar cliente por RUT |

**Ejemplo - Crear Cliente**:
```json
POST /api/clientes/
{
  "rut": "12345678-9",
  "nombre": "Juan",
  "apellido": "Pérez",
  "email": "juan@example.com",
  "telefono": "+56912345678",
  "direccion": "Av. Principal 123"
}
```

#### 📦 Productos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/productos/` | Listar todos los productos |
| POST | `/api/productos/` | Crear nuevo producto |
| GET | `/api/productos/{id}/` | Obtener detalle de producto |
| PUT | `/api/productos/{id}/` | Actualizar producto completo |
| PATCH | `/api/productos/{id}/` | Actualizar producto parcial |
| DELETE | `/api/productos/{id}/` | Eliminar producto |
| GET | `/api/productos/sin_stock/` | Productos sin stock |
| GET | `/api/productos/bajo_stock/?limite=10` | Productos con stock bajo |
| POST | `/api/productos/{id}/agregar_stock/` | Agregar stock al producto |

**Ejemplo - Crear Producto**:
```json
POST /api/productos/
{
  "codigo": "PROD001",
  "nombre": "Laptop Dell",
  "descripcion": "Laptop Dell Inspiron 15",
  "precio": 599990,
  "stock": 10
}
```

**Ejemplo - Agregar Stock**:
```json
POST /api/productos/1/agregar_stock/
{
  "cantidad": 20
}
```

#### 💰 Ventas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/ventas/` | Listar todas las ventas |
| POST | `/api/ventas/` | Crear nueva venta |
| GET | `/api/ventas/{id}/` | Obtener detalle de venta |
| DELETE | `/api/ventas/{id}/` | Eliminar venta (restaura stock) |
| GET | `/api/ventas/por_cliente/?cliente_id=1` | Ventas de un cliente |
| GET | `/api/ventas/estadisticas/` | Estadísticas generales |

**Ejemplo - Crear Venta**:
```json
POST /api/ventas/
{
  "cliente": 1,
  "observaciones": "Entrega urgente",
  "detalles": [
    {
      "producto": 1,
      "cantidad": 2,
      "precio_unitario": 599990
    },
    {
      "producto": 2,
      "cantidad": 1,
      "precio_unitario": 299990
    }
  ]
}
```

**Ejemplo - Estadísticas**:
```json
GET /api/ventas/estadisticas/

Respuesta:
{
  "total_ventas": 45,
  "monto_total": 12500000.00,
  "promedio_venta": 277777.78
}
```

#### 👤 Usuario Actual

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/users/me/` | Obtener información del usuario autenticado |

### Paginación

La API utiliza paginación automática con 10 elementos por página:

```
GET /api/clientes/?page=2
```

### Filtros y Búsqueda

Muchos endpoints soportan parámetros de búsqueda:

```
GET /api/productos/?search=laptop
GET /api/clientes/?ordering=-fecha_registro
```

### Códigos de Estado HTTP

- `200 OK` - Petición exitosa
- `201 Created` - Recurso creado exitosamente
- `204 No Content` - Recurso eliminado exitosamente
- `400 Bad Request` - Error en la petición
- `401 Unauthorized` - No autenticado
- `403 Forbidden` - Sin permisos
- `404 Not Found` - Recurso no encontrado
- `500 Internal Server Error` - Error del servidor

### Ejemplo Completo - Crear Venta con Python

```python
import requests

# 1. Obtener token
login_url = "http://127.0.0.1:8000/api/auth/login/"
login_data = {
    "username": "admin",
    "password": "admin123"
}
response = requests.post(login_url, json=login_data)
token = response.json()["access"]

# 2. Crear venta
headers = {"Authorization": f"Bearer {token}"}
venta_url = "http://127.0.0.1:8000/api/ventas/"
venta_data = {
    "cliente": 1,
    "observaciones": "Venta desde API",
    "detalles": [
        {
            "producto": 1,
            "cantidad": 2,
            "precio_unitario": 599990
        }
    ]
}
response = requests.post(venta_url, json=venta_data, headers=headers)
print(response.json())
```

### Ejemplo Completo - Listar Clientes con JavaScript

```javascript
// 1. Obtener token
const loginResponse = await fetch('http://127.0.0.1:8000/api/auth/login/', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    username: 'admin',
    password: 'admin123'
  })
});
const { access } = await loginResponse.json();

// 2. Listar clientes
const clientesResponse = await fetch('http://127.0.0.1:8000/api/clientes/', {
  headers: {'Authorization': `Bearer ${access}`}
});
const clientes = await clientesResponse.json();
console.log(clientes);
```

## 📝 Notas Importantes

- La interfaz web **no requiere autenticación** (según requisitos originales)
- La **API REST requiere autenticación JWT** para todos los endpoints
- El stock se gestiona automáticamente al crear/eliminar ventas
- Los subtotales y totales se calculan automáticamente
- Los gráficos se generan dinámicamente con datos en tiempo real
- Los tokens JWT tienen una duración de 5 horas

## 🐛 Solución de Problemas

### Error: "No module named 'django'"
```bash
pip install django
```

### Error: "Table doesn't exist"
```bash
python manage.py makemigrations
python manage.py migrate
```

### La página no carga los estilos
Verifique su conexión a internet (Tailwind CSS se carga vía CDN)

## 👨‍💻 Autor

Desarrollado como proyecto de evaluación - Sistema de Ventas Django

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

**¡Disfruta usando el Sistema de Gestión de Ventas!** 🎉
