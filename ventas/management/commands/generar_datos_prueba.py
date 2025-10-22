"""
Comando de gestión para generar datos de prueba en la base de datos.
Uso: python manage.py generar_datos_prueba
"""
from django.core.management.base import BaseCommand
from ventas.models import Cliente, Producto, Venta, DetalleVenta
from decimal import Decimal
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Genera datos de prueba para clientes, productos y ventas'

    def handle(self, *args, **kwargs):
        self.stdout.write('Generando datos de prueba...')
        
        # Limpiar datos existentes (opcional)
        self.stdout.write('Limpiando datos existentes...')
        DetalleVenta.objects.all().delete()
        Venta.objects.all().delete()
        Producto.objects.all().delete()
        Cliente.objects.all().delete()
        
        # Crear clientes
        self.stdout.write('Creando clientes...')
        clientes = [
            Cliente.objects.create(
                rut='12345678-9',
                nombre='Juan',
                apellido='Pérez',
                email='juan.perez@email.com',
                telefono='+56912345678',
                direccion='Av. Principal 123, Santiago'
            ),
            Cliente.objects.create(
                rut='98765432-1',
                nombre='María',
                apellido='González',
                email='maria.gonzalez@email.com',
                telefono='+56987654321',
                direccion='Calle Secundaria 456, Valparaíso'
            ),
            Cliente.objects.create(
                rut='11223344-5',
                nombre='Pedro',
                apellido='Martínez',
                email='pedro.martinez@email.com',
                telefono='+56911223344',
                direccion='Pasaje Los Aromos 789, Concepción'
            ),
            Cliente.objects.create(
                rut='55667788-9',
                nombre='Ana',
                apellido='López',
                email='ana.lopez@email.com',
                telefono='+56955667788',
                direccion='Av. Libertador 321, La Serena'
            ),
            Cliente.objects.create(
                rut='99887766-5',
                nombre='Carlos',
                apellido='Rodríguez',
                email='carlos.rodriguez@email.com',
                telefono='+56999887766',
                direccion='Calle Central 654, Temuco'
            ),
        ]
        self.stdout.write(self.style.SUCCESS(f'✓ Creados {len(clientes)} clientes'))
        
        # Crear productos
        self.stdout.write('Creando productos...')
        productos = [
            Producto.objects.create(
                codigo='PROD001',
                nombre='Notebook HP 15"',
                descripcion='Notebook HP 15 pulgadas, 8GB RAM, 256GB SSD',
                precio=Decimal('450000'),
                stock=15
            ),
            Producto.objects.create(
                codigo='PROD002',
                nombre='Mouse Logitech MX',
                descripcion='Mouse inalámbrico Logitech MX Master 3',
                precio=Decimal('89990'),
                stock=30
            ),
            Producto.objects.create(
                codigo='PROD003',
                nombre='Teclado Mecánico RGB',
                descripcion='Teclado mecánico con iluminación RGB',
                precio=Decimal('75000'),
                stock=25
            ),
            Producto.objects.create(
                codigo='PROD004',
                nombre='Monitor Samsung 27"',
                descripcion='Monitor Samsung curvo 27 pulgadas Full HD',
                precio=Decimal('250000'),
                stock=12
            ),
            Producto.objects.create(
                codigo='PROD005',
                nombre='Auriculares Sony WH-1000XM4',
                descripcion='Auriculares inalámbricos con cancelación de ruido',
                precio=Decimal('320000'),
                stock=20
            ),
            Producto.objects.create(
                codigo='PROD006',
                nombre='Webcam Logitech C920',
                descripcion='Webcam Full HD 1080p con micrófono',
                precio=Decimal('65000'),
                stock=18
            ),
            Producto.objects.create(
                codigo='PROD007',
                nombre='Disco Duro Externo 1TB',
                descripcion='Disco duro externo portátil 1TB USB 3.0',
                precio=Decimal('55000'),
                stock=35
            ),
            Producto.objects.create(
                codigo='PROD008',
                nombre='Memoria USB 64GB',
                descripcion='Memoria USB 3.0 de 64GB alta velocidad',
                precio=Decimal('12000'),
                stock=50
            ),
            Producto.objects.create(
                codigo='PROD009',
                nombre='Hub USB-C',
                descripcion='Hub USB-C con 4 puertos USB 3.0',
                precio=Decimal('28000'),
                stock=22
            ),
            Producto.objects.create(
                codigo='PROD010',
                nombre='Cable HDMI 2m',
                descripcion='Cable HDMI 2.0 de 2 metros 4K',
                precio=Decimal('8500'),
                stock=60
            ),
        ]
        self.stdout.write(self.style.SUCCESS(f'✓ Creados {len(productos)} productos'))
        
        # Crear ventas
        self.stdout.write('Creando ventas...')
        ventas_creadas = 0
        
        # Crear ventas aleatorias en los últimos 30 días
        for i in range(20):
            # Seleccionar cliente aleatorio
            cliente = random.choice(clientes)
            
            # Crear venta con fecha aleatoria en los últimos 30 días
            dias_atras = random.randint(0, 30)
            fecha_venta = datetime.now() - timedelta(days=dias_atras)
            
            venta = Venta.objects.create(
                cliente=cliente,
                observaciones=f'Venta de prueba #{i+1}'
            )
            
            # Cambiar la fecha de venta manualmente
            venta.fecha_venta = fecha_venta
            venta.save()
            
            # Agregar entre 1 y 4 productos a cada venta
            num_productos = random.randint(1, 4)
            productos_seleccionados = random.sample(productos, num_productos)
            
            for producto in productos_seleccionados:
                # Verificar que haya stock disponible
                if producto.stock > 0:
                    cantidad = random.randint(1, min(3, producto.stock))
                    
                    # Crear detalle de venta
                    detalle = DetalleVenta.objects.create(
                        venta=venta,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=producto.precio
                    )
                    
                    # Reducir stock
                    producto.stock -= cantidad
                    producto.save()
            
            ventas_creadas += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ Creadas {ventas_creadas} ventas con sus detalles'))
        
        # Estadísticas finales
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS('✓ Datos de prueba generados exitosamente'))
        self.stdout.write('='*50)
        self.stdout.write(f'Clientes: {Cliente.objects.count()}')
        self.stdout.write(f'Productos: {Producto.objects.count()}')
        self.stdout.write(f'Ventas: {Venta.objects.count()}')
        self.stdout.write(f'Detalles de venta: {DetalleVenta.objects.count()}')
        self.stdout.write('='*50)
