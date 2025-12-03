@echo off
echo ========================================
echo   CREAR USUARIO DE PRUEBA
echo ========================================
echo.
echo Este script te ayudara a crear un usuario de prueba
echo para acceder al sistema de ventas.
echo.
echo Presiona Ctrl+C para cancelar en cualquier momento.
echo.
python manage.py createsuperuser
echo.
echo ========================================
echo   USUARIO CREADO EXITOSAMENTE
echo ========================================
echo.
echo Ahora puedes iniciar el servidor con:
echo   python manage.py runserver
echo.
echo Y acceder al sistema en:
echo   http://127.0.0.1:8000/
echo.
pause
