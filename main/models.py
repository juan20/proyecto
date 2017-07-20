from __future__ import unicode_literals

from django.db import models
from tastypie import fields, utils
from django.utils import timezone

# Create your models here.


class Negocio(models.Model):

	id_negocio = models.AutoField(primary_key=True)	
	nombre = models.TextField(default='')
	telefono = models.TextField()
	latitud = models.TextField()
	longitud = models.TextField(default='')

class Sensor(models.Model):

	id_sensor = models.AutoField(primary_key=True)
	estado = models.TextField()

class Empleado(models.Model):

	id_empleado = models.AutoField(primary_key=True)
	nombre = models.TextField()
	direccion = models.TextField()
	telefono = models.TextField()
	flota = models.TextField()


	def __unicode__(self):
		return (('%s (%s)') % (self.nombre, self.telefono))

class Credencial(models.Model):

	id_crendencial =models.AutoField(primary_key=True)
	id_empleado = models.ForeignKey(Empleado, null=True)
	username = models.TextField()
	password = models.TextField()	

		

class Valores(models.Model):

	id_valor = models.AutoField(primary_key=True)
	date = fields.DateTimeField(readonly=True, default= timezone.now())
	sensor_mod = models.BooleanField(default=False)
	sensor_sound = models.BooleanField(default=False)
	id_sensor = models.ForeignKey(Sensor, null=True)

class Reloj(models.Model):

	id_reloj = models.AutoField(primary_key=True)
	IMEI = models.TextField()
	id_empleado = models.ForeignKey(Empleado, null=True) 

class Area(models.Model):

	id_area = models.AutoField(primary_key=True)
	nombre = models.TextField()
	estado = models.TextField()
	id_sensor = models.ForeignKey(Sensor, null=True) 
	id_negocio = models.ForeignKey(Negocio, null=True) 

class HasEmpleado(models.Model):

	id_hasEmpleado = models.AutoField(primary_key=True)
	id_empleado = models.ForeignKey(Empleado, null=True)
	id_negocio = models.ForeignKey(Negocio, null=True)  

	
