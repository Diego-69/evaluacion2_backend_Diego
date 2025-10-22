# 🎯 COMANDOS IMPORTANTES

## 📦 INSTALACIÓN Y CONFIGURACIÓN

### Instalar Django y dependencias
```bash
pip install -r requirements.txt
```

### Crear base de datos (primera vez)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Generar datos de prueba
```bash
python manage.py generar_datos_prueba
```

---

## 🚀 SERVIDOR DE DESARROLLO

### Iniciar servidor
```bash
python manage.py runserver
```

### Iniciar servidor en puerto específico
```bash
python manage.py runserver 8080
```

### Iniciar servidor accesible desde red local
```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 👤 ADMINISTRACIÓN

### Crear superusuario
```bash
python manage.py createsuperuser
```
- URL del admin: http://127.0.0.1:8000/admin/

### Cambiar contraseña de usuario
```bash
python manage.py changepassword <username>
```

---

## 🗄️ BASE DE DATOS

### Ver todas las migraciones
```bash
python manage.py showmigrations
```

### Aplicar migraciones específicas
```bash
python manage.py migrate ventas
```

### Hacer rollback a una migración anterior
```bash
python manage.py migrate ventas 0001
```

### Limpiar toda la base de datos
```bash
python manage.py flush
```

### Exportar datos a JSON
```bash
python manage.py dumpdata > backup.json
python manage.py dumpdata ventas > ventas_backup.json
```

### Importar datos desde JSON
```bash
python manage.py loaddata backup.json
```

---

## 🔍 INSPECCIÓN Y DEBUG

### Abrir shell de Django
```bash
python manage.py shell
```

### Ejemplos en el shell:
```python
# Importar modelos
from ventas.models import Cliente, Producto, Venta, DetalleVenta

# Ver todos los clientes
Cliente.objects.all()

# Crear un cliente
cliente = Cliente.objects.create(
    rut='12345678-9',
    nombre='Test',
    apellido='Usuario',
    email='test@test.com',
    telefono='+56912345678',
    direccion='Calle Test 123'
)

# Contar productos
Producto.objects.count()

# Filtrar ventas
Venta.objects.filter(cliente__nombre='Juan')

# Ordenar productos por precio
Producto.objects.order_by('-precio')[:5]

# Productos con stock bajo
Producto.objects.filter(stock__lt=10)
```

### Ver SQL de una query
```bash
python manage.py shell
```
```python
from ventas.models import Producto
print(Producto.objects.filter(stock__gt=10).query)
```

### Verificar errores en el proyecto
```bash
python manage.py check
```

---

## 🧹 LIMPIEZA Y MANTENIMIENTO

### Limpiar archivos .pyc
```bash
python manage.py clean_pyc
```

### Eliminar migraciones (CUIDADO!)
```bash
# En Windows:
del /s /q ventas\migrations\*.py
echo. > ventas\migrations\__init__.py

# Luego regenerar:
python manage.py makemigrations
```

---

## 📊 COMANDOS PERSONALIZADOS

### Generar datos de prueba
```bash
python manage.py generar_datos_prueba
```

### Ver ayuda de un comando
```bash
python manage.py help generar_datos_prueba
```

---

## 🔧 UTILIDADES

### Recolectar archivos estáticos (para producción)
```bash
python manage.py collectstatic
```

### Ver versión de Django
```bash
python -m django --version
```

### Listar todos los comandos disponibles
```bash
python manage.py help
```

---

## 🐛 DEBUGGING

### Modo verbose en servidor
```bash
python manage.py runserver --verbosity 3
```

### Ver SQL queries en shell
```python
from django.db import connection
from ventas.models import Producto

# Hacer query
productos = list(Producto.objects.all())

# Ver queries ejecutadas
print(connection.queries)
```

### Activar modo debug en settings
```python
# En config/settings.py
DEBUG = True
```

---

## 📝 TESTS (para desarrollo futuro)

### Ejecutar todos los tests
```bash
python manage.py test
```

### Ejecutar tests de una app específica
```bash
python manage.py test ventas
```

### Ejecutar un test específico
```bash
python manage.py test ventas.tests.TestCliente
```

### Tests con coverage
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 🔐 SEGURIDAD

### Generar nueva SECRET_KEY
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Verificar vulnerabilidades
```bash
python manage.py check --deploy
```

---

## 🌐 PRODUCCIÓN

### Configuraciones recomendadas para producción

1. **Variables de entorno**
```bash
set DJANGO_SETTINGS_MODULE=config.settings_prod
set SECRET_KEY=nueva_clave_secreta
set DEBUG=False
```

2. **Base de datos PostgreSQL**
```bash
pip install psycopg2
```

3. **Servidor WSGI (Gunicorn)**
```bash
pip install gunicorn
gunicorn config.wsgi:application
```

4. **Archivos estáticos**
```bash
python manage.py collectstatic --noinput
```

---

## 🚦 INICIO RÁPIDO (RESUMEN)

```bash
# Todo en uno
pip install -r requirements.txt && python manage.py migrate && python manage.py generar_datos_prueba && python manage.py runserver
```

O simplemente ejecute:
```bash
iniciar.bat
```

---

## 📌 URLS IMPORTANTES

- **Home**: http://127.0.0.1:8000/
- **Clientes**: http://127.0.0.1:8000/clientes/
- **Productos**: http://127.0.0.1:8000/productos/
- **Ventas**: http://127.0.0.1:8000/ventas/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 💡 TIPS

1. **Ctrl + C** para detener el servidor
2. Use **Ctrl + Z** para suspender en Windows CMD
3. El servidor se recarga automáticamente al editar archivos
4. Los archivos estáticos no requieren recolección en desarrollo
5. Tailwind CSS se carga desde CDN (requiere internet)

---

¡Comandos listos para usar! 🎉
