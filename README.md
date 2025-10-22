# Sistema de Gestión de Ventas - Django + Tailwind CSS

Sistema web completo de gestión de ventas desarrollado con Django y Tailwind CSS. Permite administrar clientes, productos, ventas y visualizar reportes con gráficos interactivos.

## 🚀 Características

- ✅ **CRUD completo** para Clientes, Productos y Ventas
- 📊 **Dashboard con gráficos** de productos más vendidos y clientes con más compras
- 🎨 **Diseño moderno** con Tailwind CSS
- 💾 **Base de datos SQLite** para persistencia de datos
- 📱 **Responsive Design** - Compatible con dispositivos móviles
- 🔄 **Gestión automática de stock** - Se actualiza al realizar ventas
- 📈 **Gráficos interactivos** con Chart.js

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

- **Backend**: Django 4.2.7
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

## 📝 Notas Importantes

- La aplicación **no requiere autenticación** para las vistas principales (según requisitos)
- El stock se gestiona automáticamente al crear/eliminar ventas
- Los subtotales y totales se calculan automáticamente
- Los gráficos se generan dinámicamente con datos en tiempo real

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
