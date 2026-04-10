from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import Fncvalidate_cedula

# Create your models here.
class Usuario(AbstractUser):
    """
    Modelo extendido de usuario para EcuaTrade.
    Al heredar de AbstractUser (Clase Base de Django), obtenemos automáticamente:
    - Campos core: username, email, password, is_active, is_staff.
    - Métodos de seguridad: set_password() (hash), check_password().
    - Lógica de gestión de sesiones.
    
    A esta base sólida le inyectamos los requerimientos específicos del dominio del negocio.
    """

    # Definición de tuplas para las opciones del campo 'rol'.
    # Estructura: ('valor_guardado_en_bd', 'Valor Legible en la Interfaz')
    ROLES_ECUATRADE = (
        ('comprador', 'Comprador (Cliente)'),
        ('vendedor', 'Vendedor (Tecnología/Agro)'),
    )
    
    # --- CAMPOS EXTENDIDOS DEL NEGOCIO ---

    # Campo Rol: Controla la autorización dentro de la plataforma.
    # Usamos choices para restringir los valores permitidos a nivel de base de datos.
    rol = models.CharField(
        max_length=20, 
        choices=ROLES_ECUATRADE, 
        default='comprador',
        help_text="Define la capa de permisos del usuario en la plataforma."
    )
    
    # Campo Cédula: Identificador fiscal principal.
    # Se aplica el validador personalizado que inyecta la lógica del Módulo 10.
    # unique=True garantiza integridad referencial (no clones).
    cedula = models.CharField(
        max_length=10, 
        unique=True, 
        validators=[Fncvalidate_cedula],
        help_text="Documento de identidad válido ecuatoriano."
    )
    
    # Campos logísticos (opcionales al momento del registro gracias a blank=True, null=True)
    # Se utilizarán más adelante para integraciones de envío y contacto.
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        
        return f"{self.username} - {self.get_rol_display()}"