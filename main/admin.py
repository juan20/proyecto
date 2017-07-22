from django.contrib import admin
from main.models import *

class EmpleadoAdmin(admin.TabularInline):
	model = Empleado


class CredencialAdmin(admin.ModelAdmin):
	inline = [
		EmpleadoAdmin
	]

admin.site.register(Negocio)
admin.site.register(Empleado)
admin.site.register(Credencial, CredencialAdmin)