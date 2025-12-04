# 📁 ESTRUCTURA DEL PROYECTO

```
eva2_backend/
│
├── 📄 manage.py                    # Script principal de Django
├── 📄 requirements.txt             # Dependencias del proyecto
├── 📄 iniciar.bat                  # Script de inicio automático (Windows)
├── 📄 README.md                    # Documentación completa
├── 📄 INICIO_RAPIDO.md            # Guía de inicio rápido
├── 📄 .gitignore                   # Archivos ignorados por Git
├── 💾 db.sqlite3                   # Base de datos (se crea al migrar)
│
├── 📁 config/                      # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py                # Configuración principal de Django
│   ├── urls.py                    # URLs principales del proyecto
│   ├── asgi.py                    # Configuración ASGI
│   └── wsgi.py                    # Configuración WSGI
│
├── 📁 ventas/                      # Aplicación principal
│   ├── __init__.py
│   ├── models.py                  # Modelos: Cliente, Producto, Venta, DetalleVenta
│   ├── views.py                   # Vistas CRUD y Dashboard
│   ├── forms.py                   # Formularios para modelos
│   ├── urls.py                    # URLs de la aplicación
│   ├── admin.py                   # Configuración del admin
│   ├── apps.py                    # Configuración de la app
│   ├── tests.py                   # Tests (vacío)
│   │
│   ├── 📁 migrations/              # Migraciones de base de datos
│   │   └── __init__.py
│   │
│   └── 📁 management/              # Comandos personalizados
│       ├── __init__.py
│       └── 📁 commands/
│           ├── __init__.py
│           └── generar_datos_prueba.py  # Comando para datos de prueba
│
└── 📁 templates/                   # Plantillas HTML
    ├── base.html                  # Template base con Tailwind CSS
    │
    └── 📁 ventas/                  # Templates de la app ventas
        ├── home.html              # Dashboard con gráficos
        │
        ├── cliente_list.html      # Lista de clientes
        ├── cliente_form.html      # Formulario crear/editar cliente
        ├── cliente_confirm_delete.html  # Confirmación eliminar cliente
        │
        ├── producto_list.html     # Lista de productos
        ├── producto_form.html     # Formulario crear/editar producto
        ├── producto_confirm_delete.html  # Confirmación eliminar producto
        │
        ├── venta_list.html        # Lista de ventas
        ├── venta_form.html        # Formulario crear venta (paso 1)
        ├── venta_add_productos.html  # Agregar productos (paso 2)
        ├── venta_detail.html      # Detalle completo de venta
        └── venta_confirm_delete.html  # Confirmación eliminar venta
```

---

## 🎯 COMPONENTES PRINCIPALES

### 1. MODELOS (models.py)
```
Cliente
├── rut (único)
├── nombre
├── apellido
├── email
├── telefono
├── direccion
└── fecha_registro

Producto
├── codigo (único)
├── nombre
├── descripcion
├── precio
├── stock
├── fecha_creacion
└── fecha_actualizacion

Venta
├── cliente (FK)
├── fecha_venta
├── total
└── observaciones

DetalleVenta
├── venta (FK)
├── producto (FK)
├── cantidad
├── precio_unitario
└── subtotal
```

### 2. VISTAS (views.py)
```
Dashboard:
└── home() - Muestra productos más vendidos y top clientes

Clientes:
├── cliente_list()
├── cliente_create()
├── cliente_update()
└── cliente_delete()

Productos:
├── producto_list()
├── producto_create()
├── producto_update()
└── producto_delete()

Ventas:
├── venta_list()
├── venta_create()
├── venta_add_productos()
├── venta_detail()
├── venta_delete()
└── venta_detalle_delete()
```

### 3. RUTAS (urls.py)
```
/                                    → Dashboard
/clientes/                          → Lista clientes
/clientes/crear/                    → Crear cliente
/clientes/<id>/editar/              → Editar cliente
/clientes/<id>/eliminar/            → Eliminar cliente
/productos/                         → Lista productos
/productos/crear/                   → Crear producto
/productos/<id>/editar/             → Editar producto
/productos/<id>/eliminar/           → Eliminar producto
/ventas/                            → Lista ventas
/ventas/crear/                      → Crear venta
/ventas/<id>/agregar-productos/     → Agregar productos a venta
/ventas/<id>/detalle/               → Ver detalle de venta
/ventas/<id>/eliminar/              → Eliminar venta
/ventas/detalle/<id>/eliminar/      → Eliminar detalle de venta
```

---

## 🎨 TECNOLOGÍAS

- **Backend**: Django 4.2.7
- **Base de Datos**: SQLite3
- **Frontend**: HTML5, JavaScript
- **Estilos**: Tailwind CSS (CDN)
- **Gráficos**: Chart.js (CDN)
- **Iconos**: SVG inline

---

## 🔄 FLUJO DE TRABAJO

### Crear una Venta:
1. Cliente selecciona "Nueva Venta"
2. Sistema muestra formulario para elegir cliente
3. Cliente envía formulario
4. Sistema crea venta y redirige a "Agregar Productos"
5. Cliente selecciona productos y cantidades
6. Sistema verifica stock disponible
7. Sistema actualiza stock y calcula totales
8. Cliente puede ver detalle completo de la venta

### Eliminar una Venta:
1. Cliente selecciona "Eliminar" en una venta
2. Sistema muestra confirmación
3. Cliente confirma
4. Sistema restaura stock de todos los productos
5. Sistema elimina la venta y sus detalles
6. Sistema muestra mensaje de éxito

---

## 📊 CARACTERÍSTICAS ESPECIALES

✅ **Cálculo Automático**: Los subtotales y totales se calculan automáticamente
✅ **Control de Stock**: Solo permite vender productos con stock disponible
✅ **Restauración de Stock**: Al eliminar una venta, restaura el stock
✅ **Validación de Datos**: Formularios con validación en cliente y servidor
✅ **Mensajes de Usuario**: Feedback visual para todas las acciones
✅ **Gráficos Dinámicos**: Los gráficos se generan con datos reales
✅ **Responsive Design**: Adaptable a todos los tamaños de pantalla
✅ **Navegación Intuitiva**: Menú persistente y breadcrumbs

---

## 🚀 COMANDOS DE GESTIÓN

```bash
# Instalación
pip install -r requirements.txt

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Datos de prueba
python manage.py generar_datos_prueba

# Servidor
python manage.py runserver

# Admin (opcional)
python manage.py createsuperuser
```

---

¡Todo listo para usar! 🎉
