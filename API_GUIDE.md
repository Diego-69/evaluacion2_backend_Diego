# 📡 Guía Rápida de la API REST

## 🚀 Inicio Rápido

### 1. Iniciar el servidor
```bash
python manage.py runserver
```

### 2. Acceder a Swagger
Abrir en el navegador: **http://127.0.0.1:8000/swagger/**

### 3. Crear un superusuario (si no existe)
```bash
python manage.py createsuperuser
```

## 🔐 Autenticación

### Obtener Token
```bash
POST http://127.0.0.1:8000/api/auth/login/
Content-Type: application/json

{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```

### Usar Token en Swagger
1. Haz clic en el botón **"Authorize"** en la parte superior derecha
2. Ingresa: `Bearer tu_token_aqui`
3. Haz clic en **"Authorize"**
4. Ahora puedes probar todos los endpoints

## 📋 Endpoints Disponibles

### Autenticación
- `POST /api/auth/login/` - Obtener token JWT
- `POST /api/auth/refresh/` - Refrescar token
- `POST /api/auth/verify/` - Verificar token

### Clientes
- `GET /api/clientes/` - Listar clientes
- `POST /api/clientes/` - Crear cliente
- `GET /api/clientes/{id}/` - Ver cliente
- `PUT /api/clientes/{id}/` - Actualizar cliente
- `PATCH /api/clientes/{id}/` - Actualizar parcial
- `DELETE /api/clientes/{id}/` - Eliminar cliente
- `GET /api/clientes/{id}/ventas/` - Ver ventas del cliente
- `GET /api/clientes/buscar_por_rut/?rut=xxx` - Buscar por RUT

### Productos
- `GET /api/productos/` - Listar productos
- `POST /api/productos/` - Crear producto
- `GET /api/productos/{id}/` - Ver producto
- `PUT /api/productos/{id}/` - Actualizar producto
- `PATCH /api/productos/{id}/` - Actualizar parcial
- `DELETE /api/productos/{id}/` - Eliminar producto
- `GET /api/productos/sin_stock/` - Productos sin stock
- `GET /api/productos/bajo_stock/` - Productos con stock bajo
- `POST /api/productos/{id}/agregar_stock/` - Agregar stock

### Ventas
- `GET /api/ventas/` - Listar ventas
- `POST /api/ventas/` - Crear venta
- `GET /api/ventas/{id}/` - Ver venta
- `DELETE /api/ventas/{id}/` - Eliminar venta (restaura stock)
- `GET /api/ventas/por_cliente/?cliente_id=1` - Filtrar por cliente
- `GET /api/ventas/estadisticas/` - Estadísticas generales

### Usuario
- `GET /api/users/me/` - Información del usuario actual

## 🧪 Ejemplos de Prueba con cURL

### 1. Obtener Token
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\": \"admin\", \"password\": \"admin123\"}"
```

### 2. Listar Clientes
```bash
curl -X GET http://127.0.0.1:8000/api/clientes/ ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

### 3. Crear Cliente
```bash
curl -X POST http://127.0.0.1:8000/api/clientes/ ^
  -H "Authorization: Bearer TU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"rut\": \"12345678-9\", \"nombre\": \"Juan\", \"apellido\": \"Perez\", \"email\": \"juan@example.com\", \"telefono\": \"+56912345678\", \"direccion\": \"Av. Principal 123\"}"
```

### 4. Crear Producto
```bash
curl -X POST http://127.0.0.1:8000/api/productos/ ^
  -H "Authorization: Bearer TU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"codigo\": \"PROD001\", \"nombre\": \"Laptop\", \"descripcion\": \"Laptop Dell\", \"precio\": 599990, \"stock\": 10}"
```

### 5. Crear Venta
```bash
curl -X POST http://127.0.0.1:8000/api/ventas/ ^
  -H "Authorization: Bearer TU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"cliente\": 1, \"observaciones\": \"Venta de prueba\", \"detalles\": [{\"producto\": 1, \"cantidad\": 2, \"precio_unitario\": 599990}]}"
```

### 6. Ver Estadísticas
```bash
curl -X GET http://127.0.0.1:8000/api/ventas/estadisticas/ ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

## 🐍 Ejemplo con Python

```python
import requests

# URL base
BASE_URL = "http://127.0.0.1:8000/api"

# 1. Login
response = requests.post(f"{BASE_URL}/auth/login/", json={
    "username": "admin",
    "password": "admin123"
})
token = response.json()["access"]
headers = {"Authorization": f"Bearer {token}"}

# 2. Listar clientes
response = requests.get(f"{BASE_URL}/clientes/", headers=headers)
clientes = response.json()
print("Clientes:", clientes)

# 3. Crear cliente
nuevo_cliente = {
    "rut": "98765432-1",
    "nombre": "María",
    "apellido": "González",
    "email": "maria@example.com",
    "telefono": "+56987654321",
    "direccion": "Calle Falsa 123"
}
response = requests.post(f"{BASE_URL}/clientes/", json=nuevo_cliente, headers=headers)
print("Cliente creado:", response.json())

# 4. Ver estadísticas
response = requests.get(f"{BASE_URL}/ventas/estadisticas/", headers=headers)
print("Estadísticas:", response.json())
```

## 📱 Ejemplo con JavaScript/Fetch

```javascript
const BASE_URL = "http://127.0.0.1:8000/api";

// 1. Login
async function login() {
  const response = await fetch(`${BASE_URL}/auth/login/`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      username: 'admin',
      password: 'admin123'
    })
  });
  const data = await response.json();
  return data.access;
}

// 2. Listar productos
async function listarProductos(token) {
  const response = await fetch(`${BASE_URL}/productos/`, {
    headers: {'Authorization': `Bearer ${token}`}
  });
  const productos = await response.json();
  console.log('Productos:', productos);
}

// Ejecutar
(async () => {
  const token = await login();
  await listarProductos(token);
})();
```

## ⚠️ Notas Importantes

1. **Token Expira**: Los tokens JWT expiran después de 5 horas. Usa el endpoint `/api/auth/refresh/` para renovarlos.

2. **Autenticación Requerida**: Todos los endpoints de la API requieren autenticación JWT.

3. **Formato JSON**: Todas las peticiones deben usar `Content-Type: application/json`.

4. **CORS**: Para desarrollo, el servidor permite peticiones desde cualquier origen. En producción, debes configurar CORS apropiadamente.

5. **Paginación**: Las listas están paginadas con 10 elementos por página. Usa `?page=2` para la siguiente página.

## 🔍 Herramientas Recomendadas

- **Swagger UI**: http://127.0.0.1:8000/swagger/ (Incluida)
- **ReDoc**: http://127.0.0.1:8000/redoc/ (Incluida)
- **Postman**: https://www.postman.com/downloads/
- **Insomnia**: https://insomnia.rest/download
- **Thunder Client**: Extensión de VS Code

## 📖 Documentación Adicional

- Django REST Framework: https://www.django-rest-framework.org/
- JWT: https://jwt.io/
- Swagger/OpenAPI: https://swagger.io/

---

**¡Listo para usar la API!** 🎉
