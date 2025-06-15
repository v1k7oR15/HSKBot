from django.contrib import admin
from .models import Palabra, Tipo, PerfilUsuario
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Palabra)

class PerfilInLine(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfil de usuario'

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (PerfilInLine,)
