"""
Script de prueba para verificar que la API REST funciona correctamente.
Ejecutar con: python test_api.py
"""
import requests
import json

# Configuración
BASE_URL = "http://127.0.0.1:8000/api"
USERNAME = "admin"  # Cambiar por tu usuario
PASSWORD = "admin"  # Cambiar por tu contraseña

def print_separator():
    print("\n" + "="*60 + "\n")

def test_api():
    print("🚀 Iniciando pruebas de la API REST\n")
    
    # 1. Test de Login
    print("1️⃣ Test: Autenticación JWT")
    print(f"   POST {BASE_URL}/auth/login/")
    try:
        response = requests.post(f"{BASE_URL}/auth/login/", json={
            "username": USERNAME,
            "password": PASSWORD
        })
        
        if response.status_code == 200:
            data = response.json()
            token = data.get("access")
            print("   ✅ Login exitoso")
            print(f"   Token obtenido: {token[:20]}...")
        else:
            print(f"   ❌ Error en login: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            print("\n⚠️ Por favor crea un superusuario con:")
            print("   python manage.py createsuperuser")
            return
    except Exception as e:
        print(f"   ❌ Error de conexión: {e}")
        print("   Asegúrate de que el servidor esté corriendo:")
        print("   python manage.py runserver")
        return
    
    headers = {"Authorization": f"Bearer {token}"}
    print_separator()
    
    # 2. Test de Usuario Actual
    print("2️⃣ Test: Obtener usuario actual")
    print(f"   GET {BASE_URL}/users/me/")
    response = requests.get(f"{BASE_URL}/users/me/", headers=headers)
    if response.status_code == 200:
        user = response.json()
        print(f"   ✅ Usuario: {user.get('username')}")
        print(f"   Email: {user.get('email')}")
    else:
        print(f"   ❌ Error: {response.status_code}")
    print_separator()
    
    # 3. Test de Listar Clientes
    print("3️⃣ Test: Listar clientes")
    print(f"   GET {BASE_URL}/clientes/")
    response = requests.get(f"{BASE_URL}/clientes/", headers=headers)
    if response.status_code == 200:
        data = response.json()
        count = data.get('count', len(data))
        print(f"   ✅ Total de clientes: {count}")
        if count > 0:
            results = data.get('results', data)
            if results:
                print(f"   Primer cliente: {results[0].get('nombre_completo')}")
    else:
        print(f"   ❌ Error: {response.status_code}")
    print_separator()
    
    # 4. Test de Listar Productos
    print("4️⃣ Test: Listar productos")
    print(f"   GET {BASE_URL}/productos/")
    response = requests.get(f"{BASE_URL}/productos/", headers=headers)
    if response.status_code == 200:
        data = response.json()
        count = data.get('count', len(data))
        print(f"   ✅ Total de productos: {count}")
        if count > 0:
            results = data.get('results', data)
            if results:
                print(f"   Primer producto: {results[0].get('nombre')}")
                print(f"   Stock: {results[0].get('stock')}")
    else:
        print(f"   ❌ Error: {response.status_code}")
    print_separator()
    
    # 5. Test de Productos sin Stock
    print("5️⃣ Test: Productos sin stock")
    print(f"   GET {BASE_URL}/productos/sin_stock/")
    response = requests.get(f"{BASE_URL}/productos/sin_stock/", headers=headers)
    if response.status_code == 200:
        productos = response.json()
        print(f"   ✅ Productos sin stock: {len(productos)}")
    else:
        print(f"   ❌ Error: {response.status_code}")
    print_separator()
    
    # 6. Test de Listar Ventas
    print("6️⃣ Test: Listar ventas")
    print(f"   GET {BASE_URL}/ventas/")
    response = requests.get(f"{BASE_URL}/ventas/", headers=headers)
    if response.status_code == 200:
        data = response.json()
        count = data.get('count', len(data))
        print(f"   ✅ Total de ventas: {count}")
        if count > 0:
            results = data.get('results', data)
            if results:
                print(f"   Primera venta - Cliente: {results[0].get('cliente_nombre')}")
                print(f"   Total: ${results[0].get('total')}")
    else:
        print(f"   ❌ Error: {response.status_code}")
    print_separator()
    
    # 7. Test de Estadísticas
    print("7️⃣ Test: Estadísticas de ventas")
    print(f"   GET {BASE_URL}/ventas/estadisticas/")
    response = requests.get(f"{BASE_URL}/ventas/estadisticas/", headers=headers)
    if response.status_code == 200:
        stats = response.json()
        print(f"   ✅ Estadísticas obtenidas:")
        print(f"   Total de ventas: {stats.get('total_ventas')}")
        print(f"   Monto total: ${stats.get('monto_total', 0):,.2f}")
        print(f"   Promedio por venta: ${stats.get('promedio_venta', 0):,.2f}")
    else:
        print(f"   ❌ Error: {response.status_code}")
    print_separator()
    
    # 8. Test de Crear Cliente
    print("8️⃣ Test: Crear nuevo cliente (Prueba)")
    print(f"   POST {BASE_URL}/clientes/")
    nuevo_cliente = {
        "rut": "11111111-1",
        "nombre": "Cliente",
        "apellido": "de Prueba",
        "email": "prueba@example.com",
        "telefono": "+56911111111",
        "direccion": "Dirección de Prueba 123"
    }
    response = requests.post(f"{BASE_URL}/clientes/", json=nuevo_cliente, headers=headers)
    if response.status_code == 201:
        cliente = response.json()
        cliente_id = cliente.get('id')
        print(f"   ✅ Cliente creado con ID: {cliente_id}")
        print(f"   Nombre: {cliente.get('nombre_completo')}")
        
        # 8.1 Eliminar el cliente de prueba
        print("\n   🗑️ Eliminando cliente de prueba...")
        response = requests.delete(f"{BASE_URL}/clientes/{cliente_id}/", headers=headers)
        if response.status_code == 204:
            print("   ✅ Cliente de prueba eliminado")
        else:
            print(f"   ⚠️ No se pudo eliminar el cliente de prueba (ID: {cliente_id})")
    elif response.status_code == 400:
        print(f"   ⚠️ Cliente con ese RUT ya existe (normal en pruebas repetidas)")
    else:
        print(f"   ❌ Error: {response.status_code}")
        print(f"   Respuesta: {response.text}")
    print_separator()
    
    # 9. Test de Refresh Token
    print("9️⃣ Test: Refrescar token")
    print(f"   POST {BASE_URL}/auth/refresh/")
    response = requests.post(f"{BASE_URL}/auth/login/", json={
        "username": USERNAME,
        "password": PASSWORD
    })
    if response.status_code == 200:
        refresh_token = response.json().get("refresh")
        response = requests.post(f"{BASE_URL}/auth/refresh/", json={
            "refresh": refresh_token
        })
        if response.status_code == 200:
            new_token = response.json().get("access")
            print(f"   ✅ Token refrescado exitosamente")
            print(f"   Nuevo token: {new_token[:20]}...")
        else:
            print(f"   ❌ Error: {response.status_code}")
    print_separator()
    
    # Resumen final
    print("✅ ¡Pruebas de API completadas!\n")
    print("📚 Documentación disponible en:")
    print("   - Swagger: http://127.0.0.1:8000/swagger/")
    print("   - ReDoc:   http://127.0.0.1:8000/redoc/")
    print("   - API Web: http://127.0.0.1:8000/api/")
    print("\n📖 Ver API_GUIDE.md para más información")

if __name__ == "__main__":
    test_api()
