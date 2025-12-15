# 🎯 Guía Visual Rápida - API REST

## 🚀 Inicio Rápido (3 pasos)

```
┌─────────────────────────────────────────────────────────────┐
│  1. Instalar Dependencias                                   │
│     pip install -r requirements.txt                         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  2. Iniciar Servidor                                        │
│     python manage.py runserver                              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  3. Abrir Swagger                                           │
│     http://127.0.0.1:8000/swagger/                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📡 Estructura de la API

```
http://127.0.0.1:8000/
│
├── /api/                          → API REST Principal
│   ├── /auth/
│   │   ├── /login/               → POST: Obtener token JWT
│   │   ├── /refresh/             → POST: Refrescar token
│   │   └── /verify/              → POST: Verificar token
│   │
│   ├── /users/
│   │   ├── /                     → GET: Listar usuarios
│   │   └── /me/                  → GET: Usuario actual
│   │
│   ├── /clientes/
│   │   ├── /                     → GET: Listar | POST: Crear
│   │   ├── /{id}/                → GET/PUT/PATCH/DELETE
│   │   ├── /{id}/ventas/         → GET: Ventas del cliente
│   │   └── /buscar_por_rut/      → GET: Buscar por RUT
│   │
│   ├── /productos/
│   │   ├── /                     → GET: Listar | POST: Crear
│   │   ├── /{id}/                → GET/PUT/PATCH/DELETE
│   │   ├── /sin_stock/           → GET: Sin stock
│   │   ├── /bajo_stock/          → GET: Stock bajo
│   │   └── /{id}/agregar_stock/  → POST: Añadir stock
│   │
│   └── /ventas/
│       ├── /                     → GET: Listar | POST: Crear
│       ├── /{id}/                → GET/DELETE
│       ├── /por_cliente/         → GET: Filtrar por cliente
│       └── /estadisticas/        → GET: Estadísticas
│
├── /swagger/                      → Documentación Swagger UI
├── /redoc/                        → Documentación ReDoc
└── /admin/                        → Admin de Django
```

---

## 🔐 Flujo de Autenticación

```
┌──────────────┐
│   Cliente    │
└──────┬───────┘
       │
       │ 1. POST /api/auth/login/
       │    {"username": "admin", "password": "admin123"}
       ↓
┌──────────────┐
│   Servidor   │
└──────┬───────┘
       │
       │ 2. Respuesta:
       │    {"access": "eyJ0...", "refresh": "eyJ0..."}
       ↓
┌──────────────┐
│   Cliente    │
└──────┬───────┘
       │
       │ 3. GET /api/clientes/
       │    Header: Authorization: Bearer eyJ0...
       ↓
┌──────────────┐
│   Servidor   │
└──────┬───────┘
       │
       │ 4. Respuesta:
       │    {"count": 10, "results": [...]}
       ↓
┌──────────────┐
│   Cliente    │
└──────────────┘
```

---

## 📋 Endpoints por Método HTTP

### GET (Lectura)
```
✅ /api/clientes/              → Listar clientes
✅ /api/clientes/{id}/         → Ver cliente
✅ /api/clientes/{id}/ventas/  → Ventas del cliente
✅ /api/productos/             → Listar productos
✅ /api/productos/{id}/        → Ver producto
✅ /api/productos/sin_stock/   → Sin stock
✅ /api/ventas/                → Listar ventas
✅ /api/ventas/{id}/           → Ver venta
✅ /api/ventas/estadisticas/   → Estadísticas
✅ /api/users/me/              → Usuario actual
```

### POST (Creación)
```
✅ /api/auth/login/                 → Login
✅ /api/auth/refresh/               → Refresh token
✅ /api/clientes/                   → Crear cliente
✅ /api/productos/                  → Crear producto
✅ /api/productos/{id}/agregar_stock/ → Agregar stock
✅ /api/ventas/                     → Crear venta
```

### PUT/PATCH (Actualización)
```
✅ /api/clientes/{id}/   → Actualizar cliente
✅ /api/productos/{id}/  → Actualizar producto
```

### DELETE (Eliminación)
```
✅ /api/clientes/{id}/   → Eliminar cliente
✅ /api/productos/{id}/  → Eliminar producto
✅ /api/ventas/{id}/     → Eliminar venta
```

---

## 🧪 Ejemplo de Prueba Completa

### 1. Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Respuesta:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 2. Listar Clientes
```bash
curl -X GET http://127.0.0.1:8000/api/clientes/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

**Respuesta:**
```json
{
  "count": 5,
  "results": [
    {
      "id": 1,
      "rut": "12345678-9",
      "nombre": "Juan",
      "apellido": "Pérez",
      "nombre_completo": "Juan Pérez",
      "email": "juan@example.com",
      "telefono": "+56912345678",
      "direccion": "Av. Principal 123",
      "total_ventas": 10
    }
  ]
}
```

### 3. Crear Venta
```bash
curl -X POST http://127.0.0.1:8000/api/ventas/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." \
  -H "Content-Type: application/json" \
  -d '{
    "cliente": 1,
    "observaciones": "Venta de prueba",
    "detalles": [
      {
        "producto": 1,
        "cantidad": 2,
        "precio_unitario": 599990
      }
    ]
  }'
```

**Respuesta:**
```json
{
  "id": 21,
  "cliente": 1,
  "cliente_nombre": "Juan Pérez",
  "fecha_venta": "2025-12-04T01:00:00Z",
  "total": 1199980.00,
  "observaciones": "Venta de prueba",
  "detalles": [...]
}
```

---

## 📊 Códigos de Respuesta HTTP

```
┌───────┬────────────────────────────────────────┐
│ Código│ Significado                            │
├───────┼────────────────────────────────────────┤
│  200  │ ✅ OK - Petición exitosa              │
│  201  │ ✅ Created - Recurso creado           │
│  204  │ ✅ No Content - Eliminado exitoso     │
│  400  │ ❌ Bad Request - Error en datos       │
│  401  │ ❌ Unauthorized - No autenticado      │
│  403  │ ❌ Forbidden - Sin permisos           │
│  404  │ ❌ Not Found - No encontrado          │
│  500  │ ❌ Server Error - Error del servidor  │
└───────┴────────────────────────────────────────┘
```

---

## 🎨 Usando Swagger UI

```
┌─────────────────────────────────────────────────┐
│  1. Abrir http://127.0.0.1:8000/swagger/        │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  2. Clic en "Authorize" (arriba a la derecha)   │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  3. Obtener token desde POST /api/auth/login/   │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  4. Ingresar: Bearer <tu_token_aqui>            │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  5. Clic en "Authorize"                         │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  6. ¡Listo! Ahora puedes probar todos los       │
│     endpoints directamente desde Swagger        │
└─────────────────────────────────────────────────┘
```

---

## 🗂️ Archivos del Proyecto

```
evaluacion2_backend_Diego-main/
│
├── 📁 config/
│   ├── settings.py          ← Configuración DRF/JWT
│   └── urls.py              ← URLs principales + Swagger
│
├── 📁 ventas/
│   ├── models.py            ← Modelos (sin cambios)
│   ├── serializers.py       ← ✨ NUEVO: Serializers
│   ├── viewsets.py          ← ✨ NUEVO: ViewSets
│   ├── api_urls.py          ← ✨ NUEVO: URLs de API
│   ├── views.py             ← Vistas web (sin cambios)
│   └── urls.py              ← URLs web (sin cambios)
│
├── 📁 templates/            ← Templates web (sin cambios)
│
├── 📄 requirements.txt      ← Dependencias actualizadas
├── 📄 README.md             ← Documentación actualizada
├── 📄 API_GUIDE.md          ← ✨ NUEVO: Guía de API
├── 📄 CHECKLIST_API.md      ← ✨ NUEVO: Checklist
├── 📄 RESUMEN_API.md        ← ✨ NUEVO: Resumen
├── 📄 GUIA_GITHUB.md        ← ✨ NUEVO: Guía GitHub
├── 📄 GUIA_VISUAL.md        ← ✨ NUEVO: Este archivo
└── 📄 test_api.py           ← ✨ NUEVO: Script de tests
```

---

## ✅ Checklist de Verificación Rápida

```
□ Servidor corre sin errores
□ Swagger abre correctamente
□ Login JWT funciona
□ Endpoint de clientes responde
□ Endpoint de productos responde
□ Endpoint de ventas responde
□ Estadísticas funcionan
□ Documentación actualizada
□ Código comentado
□ Listo para subir a GitHub
```

---

## 🎓 Resumen de Funcionalidades

| Característica | Implementado | Ubicación |
|----------------|--------------|-----------|
| Django REST Framework | ✅ | settings.py |
| Autenticación JWT | ✅ | api_urls.py |
| Serializers | ✅ | serializers.py |
| ViewSets | ✅ | viewsets.py |
| Routers | ✅ | api_urls.py |
| Swagger | ✅ | urls.py |
| Endpoints CRUD | ✅ | viewsets.py |
| Endpoints personalizados | ✅ | viewsets.py |
| Validaciones | ✅ | serializers.py |
| Paginación | ✅ | settings.py |
| Documentación | ✅ | *.md |
| Tests | ✅ | test_api.py |

---

## 🎯 Para Entregar

1. ✅ Código en GitHub
2. ✅ README.md actualizado
3. ✅ Servidor funcionando
4. ✅ Swagger accesible
5. ✅ API respondiendo correctamente

---

**¡Todo listo para entregar!** 🚀

Ver documentación completa en:
- `README.md` - Documentación principal
- `API_GUIDE.md` - Guía de uso
- `CHECKLIST_API.md` - Verificación completa
- `RESUMEN_API.md` - Resumen ejecutivo
