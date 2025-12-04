@echo off
echo ========================================
echo Sistema de Gestion de Ventas - Django
echo ========================================
echo.

echo [1/4] Instalando dependencias...
pip install -r requirements.txt
echo.

echo [2/4] Realizando migraciones...
python manage.py makemigrations
python manage.py migrate
echo.

echo [3/4] Generando datos de prueba...
python manage.py generar_datos_prueba
echo.

echo [4/4] Iniciando servidor...
echo.
echo ========================================
echo Servidor iniciado en: http://127.0.0.1:8000
echo Presione Ctrl+C para detener el servidor
echo ========================================
echo.
python manage.py runserver
