from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Xbee(models.Model):

	mac = models.TextField(primary_key=True)
	red = models.TextField()
	tipo = models.TextField()

class Empresa(models.Model):
	
	nombre = models.TextField()
	id_empresa = models.AutoField(primary_key=True)
	cantidad_usuarios = models.IntegerField(default=False)

class Information(models.Model):

	id_information = models.AutoField(primary_key=True)
	date = models.TextField()
	sensor_mod = models.BooleanField(default=False)
	sensor_sound = models.IntegerField(default=False)
	mac = models.ForeignKey(Xbee, null=True)
	id_empresa =models.ForeignKey(Empresa, null=True)

class usuario(models.Model):

	id_usuario = models.AutoField(primary_key=True)
	nombre = models.TextField()
	apellido = models.TextField()
	username = models.TextField()
	password = models.TextField()
	id_empresa = models.ForeignKey(Empresa, null=True)
	privilegio = models.IntegerField(default=False)
	
