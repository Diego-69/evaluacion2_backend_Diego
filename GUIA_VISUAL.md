# 🖼️ GUÍA VISUAL DE LA APLICACIÓN

## 📊 DASHBOARD (Home)

### URL: http://127.0.0.1:8000/

**Elementos principales:**
- ✅ Navbar con logo "Sistema de Ventas" y menú de navegación
- ✅ Título: "📊 Dashboard de Ventas"
- ✅ 3 Cards de acceso rápido:
  - "Nueva Venta" (verde)
  - "Nuevo Cliente" (azul)
  - "Nuevo Producto" (morado)

**Sección: Productos Más Vendidos**
- ✅ Icono de gráfico de barras
- ✅ Tabla con: #, Producto, Unidades Vendidas
- ✅ Gráfico de barras azul con Chart.js
- ✅ Muestra top 10 productos

**Sección: Clientes con Más Ventas**
- ✅ Icono de personas
- ✅ Tabla con: #, Cliente, Total Compras, # Ventas
- ✅ Gráfico circular (doughnut) multicolor
- ✅ Muestra top 10 clientes

**Footer:**
- ✅ "© 2025 Sistema de Ventas - Desarrollado con Django y Tailwind CSS"

---

## 👥 GESTIÓN DE CLIENTES

### Lista de Clientes
**URL: http://127.0.0.1:8000/clientes/**

**Elementos:**
- ✅ Título: "👥 Gestión de Clientes"
- ✅ Botón verde "Nuevo Cliente" (esquina superior derecha)
- ✅ Tabla con fondo degradado azul-morado en header:
  - Columnas: RUT, Nombre, Email, Teléfono, Fecha Registro, Acciones
  - Iconos de editar (lápiz azul) y eliminar (basura roja)
- ✅ Hover effect: fila cambia a gris claro
- ✅ Estado vacío: Icono de personas, mensaje y botón "Nuevo Cliente"

### Crear/Editar Cliente
**URL: http://127.0.0.1:8000/clientes/crear/**

**Elementos:**
- ✅ Breadcrumb: "← Volver a Clientes"
- ✅ Título: "Crear Cliente" o "Editar Cliente"
- ✅ Formulario en card blanco con sombra:
  - Grid 2 columnas en desktop
  - Campos: RUT*, Nombre*, Apellido*, Email*, Teléfono*, Dirección*
  - Placeholders descriptivos
  - Campos marcados con asterisco rojo
- ✅ Botones: "Cancelar" (gris) y "Crear/Editar Cliente" (azul)

### Eliminar Cliente
**URL: http://127.0.0.1:8000/clientes/<id>/eliminar/**

**Elementos:**
- ✅ Alert rojo con advertencia
- ✅ Texto: "¿Está seguro que desea eliminar este cliente?"
- ✅ Card con información del cliente (fondo gris claro)
- ✅ Botones: "Cancelar" (gris) y "Sí, Eliminar" (rojo)

---

## 📦 GESTIÓN DE PRODUCTOS

### Lista de Productos
**URL: http://127.0.0.1:8000/productos/**

**Elementos:**
- ✅ Título: "📦 Gestión de Productos"
- ✅ Botón morado "Nuevo Producto"
- ✅ Tabla con fondo degradado morado-rosa en header:
  - Columnas: Código, Nombre, Descripción, Precio, Stock, Acciones
  - Badges de precio (verde)
  - Badges de stock con colores semánticos:
    - Verde: >10 unidades
    - Amarillo: 1-10 unidades
    - Rojo: Sin stock
- ✅ Iconos de editar y eliminar

### Crear/Editar Producto
**URL: http://127.0.0.1:8000/productos/crear/**

**Elementos:**
- ✅ Breadcrumb: "← Volver a Productos"
- ✅ Título: "Crear Producto" o "Editar Producto"
- ✅ Formulario en card:
  - Código* y Nombre* (2 columnas)
  - Descripción* (ancho completo)
  - Precio* (con icono $) y Stock* (2 columnas)
- ✅ Botones: "Cancelar" y "Crear/Editar Producto" (morado)

### Eliminar Producto
**URL: http://127.0.0.1:8000/productos/<id>/eliminar/**

**Elementos:**
- ✅ Alert rojo
- ✅ Información del producto
- ✅ Botones de confirmación

---

## 💰 GESTIÓN DE VENTAS

### Lista de Ventas
**URL: http://127.0.0.1:8000/ventas/**

**Elementos:**
- ✅ Título: "💰 Gestión de Ventas"
- ✅ Botón verde "Nueva Venta"
- ✅ Tabla con fondo degradado verde en header:
  - Columnas: # Venta, Cliente, Fecha, Total, Acciones
  - Badge grande de total (verde, negrita)
  - 3 iconos de acción:
    - Ojo azul: Ver detalle
    - Plus verde: Agregar productos
    - Basura roja: Eliminar

### Crear Venta (Paso 1)
**URL: http://127.0.0.1:8000/ventas/crear/**

**Elementos:**
- ✅ Breadcrumb: "← Volver a Ventas"
- ✅ Título: "Crear Venta"
- ✅ Subtítulo: "Paso 1: Seleccione el cliente para la venta"
- ✅ Formulario:
  - Select de Cliente*
  - Textarea de Observaciones
- ✅ Alert azul informativo sobre el proceso
- ✅ Botón "Continuar →" (verde)

### Agregar Productos (Paso 2)
**URL: http://127.0.0.1:8000/ventas/<id>/agregar-productos/**

**Layout en 2 columnas:**

**Columna Izquierda (Formulario - sticky):**
- ✅ Card blanco con "Agregar Producto"
- ✅ Select de Producto*
- ✅ Input de Cantidad*
- ✅ Botón "Agregar Producto" (verde, ancho completo)
- ✅ Resumen del Total (grande, verde)
- ✅ Botón "Finalizar Venta" (azul)

**Columna Derecha (Lista):**
- ✅ Card "Productos en la Venta"
- ✅ Tabla con productos agregados:
  - Producto, Cantidad, Precio Unit., Subtotal, Acción
  - Icono de eliminar por producto
- ✅ Estado vacío con mensaje

### Ver Detalle de Venta
**URL: http://127.0.0.1:8000/ventas/<id>/detalle/**

**Elementos:**
- ✅ Header con # Venta, fecha y badge de total
- ✅ Card "Información del Cliente":
  - Grid con nombre, RUT, email, teléfono
  - Observaciones (si existen)
- ✅ Card "Productos":
  - Tabla completa con código de producto
  - Fila final con TOTAL en negrita
- ✅ Botones: "Agregar Más Productos" y "Ver Todas las Ventas"

### Eliminar Venta
**URL: http://127.0.0.1:8000/ventas/<id>/eliminar/**

**Elementos:**
- ✅ Alert rojo sobre restauración de stock
- ✅ Información de la venta (# Venta, Cliente, Fecha, Total)
- ✅ Botones de confirmación

---

## 🎨 ELEMENTOS DE DISEÑO COMUNES

### Navbar
```
┌────────────────────────────────────────────────────────┐
│ 🛒 Sistema de Ventas  📊Inicio 👥Clientes 📦Productos 💰Ventas │
└────────────────────────────────────────────────────────┘
```
- Fondo: Degradado azul-morado
- Texto: Blanco
- Hover: Fondo blanco semi-transparente

### Mensajes Flash
**Éxito (verde):**
```
┌────────────────────────────────────────┐
│ ✓ Cliente creado exitosamente.        │
└────────────────────────────────────────┘
```

**Error (rojo):**
```
┌────────────────────────────────────────┐
│ ✗ Stock insuficiente. Solo hay 5...   │
└────────────────────────────────────────┘
```

### Botones
- **Primario**: Fondo sólido con hover más oscuro
- **Secundario**: Borde con hover fondo gris claro
- **Peligro**: Rojo para acciones destructivas
- **Con iconos**: SVG a la izquierda del texto

### Cards
- Fondo blanco
- Sombra sutil (shadow-md)
- Bordes redondeados (rounded-lg)
- Padding generoso (p-6)

### Tablas
- Header con color temático degradado
- Filas alternadas (striped) al hover
- Texto bien espaciado
- Responsive: scroll horizontal en móvil

### Formularios
- Labels en gris oscuro, bold
- Inputs con borde gris, focus azul
- Errores en rojo bajo el campo
- Placeholders descriptivos

---

## 📱 RESPONSIVE

### Desktop (>1024px)
- Layout a 2-3 columnas
- Tablas completas
- Gráficos lado a lado con tablas
- Menú completo en navbar

### Tablet (768px - 1024px)
- Layout a 2 columnas
- Tablas con scroll si necesario
- Gráficos en columna completa

### Móvil (<768px)
- Layout a 1 columna
- Menú hamburguesa
- Botones de ancho completo
- Cards apiladas verticalmente
- Tablas con scroll horizontal

---

## 🎯 FLUJO DE USUARIO TÍPICO

### Escenario: Registrar una venta

1. **Inicio** → Usuario ve dashboard
2. **Click** "Nueva Venta" (card verde)
3. **Formulario** → Selecciona cliente
4. **Continuar** → Va a agregar productos
5. **Agregar** → Selecciona producto y cantidad
6. **Repetir** → Agrega más productos si desea
7. **Finalizar** → Ve detalle completo de venta
8. **Regresar** → Vuelve a lista de ventas

### Navegación rápida
- Desde cualquier vista → Click logo → Home
- Desde cualquier vista → Click menú → Módulo deseado
- Breadcrumbs → Volver a lista

---

## ✨ DETALLES VISUALES

### Iconos SVG
- ✅ Carrito de compras: Ventas
- ✅ Personas: Clientes
- ✅ Caja: Productos
- ✅ Gráficos: Dashboard
- ✅ Lápiz: Editar
- ✅ Basura: Eliminar
- ✅ Ojo: Ver
- ✅ Plus: Agregar

### Animaciones
- ✅ Hover: scale(1.02) en cards
- ✅ Transitions suaves (duration-200)
- ✅ Fade in de mensajes
- ✅ Ripple effect en botones

### Tipografía
- ✅ Títulos: font-bold, text-3xl
- ✅ Subtítulos: font-medium, text-xl
- ✅ Cuerpo: text-sm/text-base
- ✅ Labels: text-sm font-medium

---

¡Interfaz moderna y profesional! 🎨
