# 🚀 INICIO RÁPIDO - Sistema de Ventas

## Opción 1: Inicio Automático (Recomendado)

Simplemente ejecute el archivo `iniciar.bat` haciendo doble clic en él.

El script automáticamente:
1. ✅ Instalará las dependencias
2. ✅ Creará la base de datos
3. ✅ Generará datos de prueba
4. ✅ Iniciará el servidor

Luego abra su navegador en: **http://127.0.0.1:8000**

---

## Opción 2: Inicio Manual

Abra una terminal (CMD o PowerShell) en esta carpeta y ejecute:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Crear base de datos
python manage.py makemigrations
python manage.py migrate

# 3. (Opcional) Generar datos de prueba
python manage.py generar_datos_prueba

# 4. Iniciar servidor
python manage.py runserver
```

Abra su navegador en: **http://127.0.0.1:8000**

---

## 🎯 Navegación de la Aplicación

### Home (Dashboard)
- **URL**: http://127.0.0.1:8000/
- Ver productos más vendidos con gráfico
- Ver clientes con más ventas con gráfico
- Accesos rápidos

### Clientes
- **Listar**: http://127.0.0.1:8000/clientes/
- **Crear**: http://127.0.0.1:8000/clientes/crear/
- Editar y eliminar desde la lista

### Productos
- **Listar**: http://127.0.0.1:8000/productos/
- **Crear**: http://127.0.0.1:8000/productos/crear/
- Editar y eliminar desde la lista

### Ventas
- **Listar**: http://127.0.0.1:8000/ventas/
- **Crear**: http://127.0.0.1:8000/ventas/crear/
- Ver detalle, agregar productos y eliminar desde la lista

---

## 🔧 Comandos Útiles

### Crear un superusuario (para acceder al admin de Django)
```bash
python manage.py createsuperuser
```
Luego acceda a: http://127.0.0.1:8000/admin/

### Limpiar base de datos y regenerar datos
```bash
python manage.py flush
python manage.py generar_datos_prueba
```

### Ver todas las migraciones
```bash
python manage.py showmigrations
```

---

## 📊 Datos de Prueba

Si ejecutó `python manage.py generar_datos_prueba`, se crearon:

- **5 Clientes** con nombres como Juan Pérez, María González, etc.
- **10 Productos** tecnológicos (notebooks, mouse, teclados, etc.)
- **20 Ventas** aleatorias distribuidas en los últimos 30 días

Estos datos permiten ver inmediatamente los gráficos y funcionalidades.

---

## ❓ Problemas Comunes

### "python no se reconoce como comando"
- Instale Python desde https://www.python.org/
- Durante la instalación, marque "Add Python to PATH"

### "pip no se reconoce como comando"
```bash
python -m pip install -r requirements.txt
```

### Error de permisos en Windows
- Ejecute CMD o PowerShell como Administrador
- O use: `py` en lugar de `python`

### No se ven los estilos (Tailwind)
- Verifique su conexión a internet
- Tailwind CSS se carga desde CDN

---

## 🎨 Características Destacadas

✅ **Diseño Moderno**: Interfaz limpia con Tailwind CSS
✅ **Responsive**: Funciona en móviles, tablets y desktop
✅ **Gráficos Interactivos**: Chart.js para visualización de datos
✅ **Control de Stock**: Actualización automática al vender
✅ **Validaciones**: Formularios con validación completa
✅ **UX Optimizada**: Mensajes de confirmación y alertas
✅ **Sin Autenticación**: Acceso directo a todas las funciones

---

## 📞 Soporte

Para más información, consulte el archivo `README.md` completo.

¡Disfrute usando el Sistema de Gestión de Ventas! 🎉
