from __future__ import unicode_literals

from django.db import models
from tastypie import fields, utils
from django.utils import timezone
from datetime import datetime
# Create your models here.


class Negocio(models.Model):

	id_negocio = models.AutoField(primary_key=True)	
	nombre = models.TextField(default='')
	telefono = models.TextField()
	latitud = models.TextField()
	longitud = models.TextField(default='')

	def __str__(self):
		return (('%s (%s)') % (self.nombre, self.telefono))

class Sensor(models.Model):

	id_sensor = models.AutoField(primary_key=True)
	estado = models.TextField()

	def __str__(self):
		return (('%s') % (self.id_sensor))

class Empleado(models.Model):

	id_empleado = models.AutoField(primary_key=True)
	nombre = models.TextField()
	direccion = models.TextField()
	telefono = models.TextField()
	flota = models.TextField()


	def __str__(self):
		return (('%s (%s)') % (self.nombre, self.telefono))

class Credencial(models.Model):

	id_crendencial =models.AutoField(primary_key=True)
	id_empleado = models.ForeignKey(Empleado, null=True)
	username = models.TextField()
	password = models.TextField()

	def __str__(self):
		return (('%s (%s)') % (self.id_empleado.nombre, self.username))

class Valores(models.Model):

	id_valor = models.AutoField(primary_key=True)
	date = models.DateTimeField(default= datetime.now)
	sensor_mod = models.BooleanField(default=False)
	sensor_sound = models.BooleanField(default=False)
	id_sensor = models.ForeignKey(Sensor, null=True)

	# de eso me gustaria devolver el id y los valores de ambos sensores
	#haz l mismo

	def __str__(self):
		return (('%s (%s) (%s)') % (self.id_valor, self.sensor_mod, self.sensor_sound))


class Reloj(models.Model):

	id_reloj = models.AutoField(primary_key=True)
	IMEI = models.TextField()
	id_empleado = models.ForeignKey(Empleado, null=True) 

	def __str__(self):
		return (('%s') % (self.IMEI))



class Area(models.Model):

	id_area = models.AutoField(primary_key=True)
	nombre = models.TextField()
	estado = models.TextField()
	id_sensor = models.ForeignKey(Sensor, null=True) 
	id_negocio = models.ForeignKey(Negocio, null=True)

	def __str__(self):
		return (('%s (%s)') % (self.nombre, self.estado))

class HasEmpleado(models.Model):

	id_hasEmpleado = models.AutoField(primary_key=True)
	id_empleado = models.ForeignKey(Empleado, null=True)
	id_negocio = models.ForeignKey(Negocio, null=True)  

	def __str__(self):
		return (('%s (%s)') % (self.id_empleado.nombre, self.id_negocio.nombre))
	# a esto me referia  con saber si se puede usar valores de la case de sus id y no de su clases por que no se como identificarlos 
	# por ejemplo devolver el nombre del empleado y el nombre de la empresa

	
