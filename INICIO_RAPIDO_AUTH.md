# ⚡ INICIO RÁPIDO - Sistema de Autenticación

## 🚀 3 Pasos para Empezar

### 1️⃣ Crear Usuario (IMPORTANTE)
```cmd
python manage.py createsuperuser
```
**O ejecuta:** `crear_usuario.bat`

Ingresa:
- Nombre de usuario: `admin`
- Email: `admin@ejemplo.com`
- Contraseña: (la que quieras, mínimo 8 caracteres)

---

### 2️⃣ Iniciar Servidor
```cmd
python manage.py runserver
```

---

### 3️⃣ Acceder
Abre tu navegador en:
```
http://127.0.0.1:8000/
```

Serás redirigido automáticamente a la página de login.

---

## 🎯 Opciones de Acceso

### Opción A: Login con Usuario Existente
1. Ir a la página de login
2. Ingresar usuario y contraseña
3. Click en "Iniciar Sesión"
4. ¡Listo! Ya estás dentro 🎉

### Opción B: Crear Nueva Cuenta
1. En la página de login, click en "Crear una cuenta nueva"
2. Completar el formulario de registro
3. Click en "Crear Cuenta"
4. ¡Automáticamente entrarás al sistema! 🎉

---

## 📋 Datos de Prueba (si usas el comando generar_datos_prueba)

Si ya tienes datos de prueba, puedes usar cualquier usuario creado previamente.

---

## ❓ Problemas Comunes

### "No puedo acceder a ninguna página"
✅ **Solución:** Es normal, TODAS las páginas requieren login ahora.  
   → Ve a `http://127.0.0.1:8000/login/`

### "No tengo usuario"
✅ **Solución:** Crea uno con:
   ```cmd
   python manage.py createsuperuser
   ```

### "Olvidé mi contraseña"
✅ **Solución:** Crea un nuevo usuario o restablece desde admin:
   ```cmd
   python manage.py changepassword <nombre_usuario>
   ```

---

## 🎨 Características del Sistema

- ✅ Login con validación
- ✅ Registro de nuevos usuarios
- ✅ Logout seguro
- ✅ Todas las páginas protegidas
- ✅ Diseño moderno con TailwindCSS
- ✅ Responsive (móvil y desktop)
- ✅ Mensajes informativos
- ✅ Navbar con nombre de usuario

---

## 📚 Más Información

Lee los archivos:
- `AUTENTICACION_README.md` - Documentación completa
- `RESUMEN_IMPLEMENTACION.md` - Detalles técnicos

---

## ✨ ¡Eso es todo!

Tu sistema está completamente funcional y listo para usar.

**¡Disfruta tu aplicación de ventas con autenticación! 🚀**
