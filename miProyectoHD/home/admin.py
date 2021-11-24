from django.contrib import admin

from .models import Paciente, Tessiu

# Register your models here.

class TessiueAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'temperatura', 'inflamation','name')

admin.site.register(Tessiu, TessiueAdmin)


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Paciente, PacienteAdmin)
