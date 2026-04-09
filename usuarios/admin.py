from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdminPersonalizado(UserAdmin):
    # 1. Para la pantalla de EDITAR (El que ya teníamos)
    fieldsets = UserAdmin.fieldsets + (
        ('Datos de EcuaTrade', {'fields': ('cedula', 'rol')}), 
    )
    
    # 2. Para la pantalla de CREAR (¡Esto evita el error de la pantalla roja!)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos de EcuaTrade', {'fields': ('cedula', 'rol')}),
    )
    
    # 3. Para verlos en la tabla principal
    list_display = ('username', 'email', 'cedula', 'rol', 'is_staff')

admin.site.register(Usuario, UsuarioAdminPersonalizado)