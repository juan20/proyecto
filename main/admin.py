from django.contrib import admin
from main.models import *

class EmpleadoInline(admin.TabularInline):
	model = Empleado

class SensorInline(admin.TabularInline):
	model = Sensor

class NegocioInline(admin.TabularInline):
	model = Negocio

class CredencialInline(admin.TabularInline):
	model = Credencial

class RelojInline(admin.TabularInline):
	model = Reloj

class HasEmpleadoInline(admin.TabularInline):
	model = HasEmpleado

class ValorInline(admin.TabularInline):
	model  = Valores

class AreaInline(admin.TabularInline):
	model  = Area

class NegocioAdmin(admin.ModelAdmin):
	model = Negocio
	inlines = [
		HasEmpleadoInline,
		AreaInline,
	]

class CredencialAdmin(admin.ModelAdmin):
	model = Credencial

class SensorAdmin(admin.ModelAdmin):
	model = Sensor
	inlines = [ValorInline,
		AreaInline,
		]

class RelojAdmin(admin.ModelAdmin):
	model = Reloj

class AreaAdmin(admin.ModelAdmin):
	model = Area
	

class ValorAdmin(admin.ModelAdmin): 
	model = Valores

class RelojAdmin(admin.ModelAdmin):
	model = Reloj


class HasEmpleadoAdmin(admin.ModelAdmin):
	model = HasEmpleado

class EmpleadoAdmin(admin.ModelAdmin):
	model = Empleado
	inlines = [
		CredencialInline,
		HasEmpleadoInline,
		RelojInline,
	]


admin.site.register(Negocio, NegocioAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Credencial, CredencialAdmin)
admin.site.register(Valores, ValorAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Reloj, RelojAdmin)
admin.site.register(HasEmpleado, HasEmpleadoAdmin)
admin.site.register(Area, AreaAdmin)



