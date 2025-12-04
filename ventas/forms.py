"""
Formularios para la aplicación de ventas.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Cliente, Producto, Venta, DetalleVenta


# ==================== FORMULARIOS DE AUTENTICACIÓN ====================

class RegistroForm(UserCreationForm):
    """
    Formulario personalizado para registro de usuarios.
    Incluye campos adicionales y estilos de TailwindCSS.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    first_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
            'placeholder': 'Nombre'
        })
    )
    last_name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
            'placeholder': 'Apellido'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
                'placeholder': 'Nombre de usuario'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar estilos de TailwindCSS a los campos de contraseña
        self.fields['password1'].widget.attrs.update({
            'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
            'placeholder': 'Confirmar contraseña'
        })
        
        # Personalizar las etiquetas en español
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['email'].label = 'Correo electrónico'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        
        # Personalizar los mensajes de ayuda
        self.fields['username'].help_text = 'Máximo 150 caracteres. Letras, dígitos y @/./+/-/_ únicamente.'
        self.fields['password1'].help_text = 'Mínimo 8 caracteres. No puede ser muy similar a tu información personal.'
        self.fields['password2'].help_text = 'Ingresa la misma contraseña para verificación.'
    
    def clean_email(self):
        """Validar que el email no esté registrado."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    def save(self, commit=True):
        """Guardar el usuario con los datos adicionales."""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    """
    Formulario personalizado para login de usuarios.
    Aplica estilos de TailwindCSS.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
            'placeholder': 'Nombre de usuario'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-gray-300 shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200',
            'placeholder': 'Contraseña'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'


# ==================== FORMULARIOS DE VENTAS ====================


class ClienteForm(forms.ModelForm):
    """Formulario para crear y editar clientes."""
    
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'email', 'telefono', 'direccion']
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'Ej: 12345678-9'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'Nombre del cliente'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'Apellido del cliente'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'email@ejemplo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': '+56912345678'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'Dirección completa'
            }),
        }


class ProductoForm(forms.ModelForm):
    """Formulario para crear y editar productos."""
    
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion', 'precio', 'stock']
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'Ej: PROD001'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'Descripción del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': '0',
                'min': '0'
            }),
        }


class VentaForm(forms.ModelForm):
    """Formulario para crear y editar ventas."""
    
    class Meta:
        model = Venta
        fields = ['cliente', 'observaciones']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'Observaciones adicionales (opcional)'
            }),
        }


class DetalleVentaForm(forms.ModelForm):
    """Formulario para agregar productos a una venta."""
    
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': '1',
                'min': '1',
                'value': '1'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mostrar solo productos con stock disponible
        self.fields['producto'].queryset = Producto.objects.filter(stock__gt=0)
