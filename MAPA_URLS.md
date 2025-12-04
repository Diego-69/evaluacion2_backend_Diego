# 🗺️ MAPA DE URLS - Sistema de Ventas con Autenticación

## 🔐 URLs de Autenticación (Públicas)

| URL | Nombre | Descripción | Requiere Login |
|-----|--------|-------------|----------------|
| `/login/` | `login` | Página de inicio de sesión | ❌ No |
| `/registro/` | `registro` | Página de registro de usuarios | ❌ No |
| `/logout/` | `logout` | Cerrar sesión | ✅ Sí |

---

## 🏠 URLs Principales (Protegidas)

| URL | Nombre | Descripción | Requiere Login |
|-----|--------|-------------|----------------|
| `/` | `home` | Página principal con gráficos | ✅ Sí |

---

## 👥 URLs de Clientes (Protegidas)

| URL | Nombre | Descripción | Requiere Login |
|-----|--------|-------------|----------------|
| `/clientes/` | `cliente_list` | Lista de clientes | ✅ Sí |
| `/clientes/crear/` | `cliente_create` | Crear nuevo cliente | ✅ Sí |
| `/clientes/<id>/editar/` | `cliente_update` | Editar cliente | ✅ Sí |
| `/clientes/<id>/eliminar/` | `cliente_delete` | Eliminar cliente | ✅ Sí |

---

## 📦 URLs de Productos (Protegidas)

| URL | Nombre | Descripción | Requiere Login |
|-----|--------|-------------|----------------|
| `/productos/` | `producto_list` | Lista de productos | ✅ Sí |
| `/productos/crear/` | `producto_create` | Crear nuevo producto | ✅ Sí |
| `/productos/<id>/editar/` | `producto_update` | Editar producto | ✅ Sí |
| `/productos/<id>/eliminar/` | `producto_delete` | Eliminar producto | ✅ Sí |

---

## 💰 URLs de Ventas (Protegidas)

| URL | Nombre | Descripción | Requiere Login |
|-----|--------|-------------|----------------|
| `/ventas/` | `venta_list` | Lista de ventas | ✅ Sí |
| `/ventas/crear/` | `venta_create` | Crear nueva venta | ✅ Sí |
| `/ventas/<id>/agregar-productos/` | `venta_add_productos` | Agregar productos a venta | ✅ Sí |
| `/ventas/<id>/detalle/` | `venta_detail` | Ver detalle de venta | ✅ Sí |
| `/ventas/<id>/eliminar/` | `venta_delete` | Eliminar venta | ✅ Sí |
| `/ventas/detalle/<id>/eliminar/` | `venta_detalle_delete` | Eliminar producto de venta | ✅ Sí |

---

## 🔄 Comportamiento de Redirección

### Sin Sesión Activa:
```
Usuario intenta acceder a cualquier URL protegida
    ↓
Redirige a: /login/?next=/url-solicitada/
    ↓
Después de login exitoso
    ↓
Redirige a la URL solicitada originalmente
```

### Con Sesión Activa:
```
Usuario accede a /login/ o /registro/
    ↓
Redirige automáticamente a: / (home)
```

### Después de Logout:
```
Usuario hace click en "Salir"
    ↓
Cierra sesión
    ↓
Redirige a: /login/
```

---

## 🎯 URLs de Acceso Rápido

### Para Desarrollo:
```
Home:           http://127.0.0.1:8000/
Login:          http://127.0.0.1:8000/login/
Registro:       http://127.0.0.1:8000/registro/
Clientes:       http://127.0.0.1:8000/clientes/
Productos:      http://127.0.0.1:8000/productos/
Ventas:         http://127.0.0.1:8000/ventas/
Admin:          http://127.0.0.1:8000/admin/
```

---

## 🔒 Seguridad de URLs

| Tipo de URL | Protección | Comportamiento |
|-------------|------------|----------------|
| **Autenticación** | Pública | Accesible sin login |
| **CRUD (Todas)** | `@login_required` | Redirige a login si no autenticado |
| **Admin** | Django Admin | Requiere superusuario |

---

## 📱 Navegación en la UI

### Navbar (Usuario Logueado):
- 📊 **Inicio** → `/`
- 👥 **Clientes** → `/clientes/`
- 📦 **Productos** → `/productos/`
- 💰 **Ventas** → `/ventas/`
- 🚪 **Salir** → `/logout/`

### Desde Login:
- 🔐 **Iniciar Sesión** → Formulario de login
- ✨ **Crear cuenta** → `/registro/`

### Desde Registro:
- ✨ **Crear Cuenta** → Formulario de registro
- 🔐 **Iniciar sesión** → `/login/`

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Crear Cliente
```
1. Login en /login/
2. Click en "Clientes" (navbar)
3. Click en "Crear Cliente"
4. Completar formulario
5. Submit → Redirige a /clientes/
```

### Ejemplo 2: Crear Venta
```
1. Login en /login/
2. Click en "Ventas" (navbar)
3. Click en "Nueva Venta"
4. Seleccionar cliente
5. Submit → Redirige a agregar productos
6. Agregar productos
7. Ver detalle de venta
```

### Ejemplo 3: Flujo Completo
```
1. Acceder a /
2. Auto-redirige a /login/
3. Click en "Crear cuenta"
4. Completar registro en /registro/
5. Auto-login y redirige a /
6. Ver dashboard con gráficos
7. Navegar por el sistema
8. Click en "Salir" para logout
```

---

## 🧪 URLs para Testing

### Test de Restricción:
1. Cerrar sesión (logout)
2. Intentar acceder a: `/clientes/`
3. **Resultado esperado:** Redirige a `/login/?next=/clientes/`
4. Iniciar sesión
5. **Resultado esperado:** Redirige a `/clientes/`

### Test de Redirección:
1. Iniciar sesión
2. Intentar acceder a: `/login/`
3. **Resultado esperado:** Redirige a `/` (home)

---

## 📊 Resumen de URLs

```
Total de URLs: 17
├── Autenticación: 3
│   ├── Login: 1
│   ├── Registro: 1
│   └── Logout: 1
├── Principal: 1
│   └── Home: 1
├── Clientes: 4
│   ├── Listar: 1
│   ├── Crear: 1
│   ├── Editar: 1
│   └── Eliminar: 1
├── Productos: 4
│   ├── Listar: 1
│   ├── Crear: 1
│   ├── Editar: 1
│   └── Eliminar: 1
└── Ventas: 6
    ├── Listar: 1
    ├── Crear: 1
    ├── Agregar productos: 1
    ├── Ver detalle: 1
    ├── Eliminar venta: 1
    └── Eliminar detalle: 1
```

---

## ✅ URLs Completamente Funcionales

- ✅ Todas las URLs implementadas
- ✅ Todas las URLs protegidas (excepto login/registro)
- ✅ Todas las redirecciones funcionando
- ✅ Parámetro `next` funcionando correctamente
- ✅ Sin URLs rotas
- ✅ Sin conflictos de rutas

---

**¡Sistema de URLs completamente funcional! 🚀**
