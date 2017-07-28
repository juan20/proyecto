from tastypie.resources import ModelResource,Resource
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
import time
from tastypie import fields, utils
from main.models import *
from datetime import datetime

class ModulosResource(ModelResource):


	class Meta:

		queryset = Area.objects.all()
		resource_name = 'modulo'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		negocio = int(bundle.request.GET['idne'])
		area = Area.objects.filter(id_negocio_id = negocio)
		result = {}
		result=[]

		for i in area:
			aux = {}
			aux ['id'] = i.id_area
			aux ['nombre'] = i.nombre
			senso = Sensor.objects.filter(id_sensor = i.id_sensor_id)[0]
			valos = Valores.objects.filter(id_sensor = senso)
			valo = valos.order_by('-id_valor')[0]
			aux ['sensormov'] = valo.sensor_mod
			aux ['sensorson'] = valo.sensor_sound
			result.append(aux) 
 

		return result

class NegocioResource(ModelResource):


	class Meta:

		queryset = Negocio.objects.all()
		resource_name = 'negocio'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		negocio = int(bundle.request.GET['idne'])
		neg = Negocio.objects.filter(id_negocio = negocio)[0]
		result = {}
		result['nombre'] = neg.nombre
		result['latitud'] = neg.latitud
		result['longitud'] = neg.longitud
		sensores = Area.objects.filter(id_negocio_id = negocio)
		result['sensores'] = len(sensores)
		result['servidores'] = 2



		return result

class AreaResource(ModelResource):


	class Meta:

		queryset = Area.objects.all()
		resource_name = 'area'
		authorization = Authorization()
		list_allowed_methods = ['post', 'get']

	def dehydrate(self, bundle):

		area = int(bundle.request.GET['ida'])
		estad = str(bundle.request.GET['est'])
		result = Area.objects.filter(id_area = area)[0] 
		result.estado = estad
		result.save() 

		return result.estado


class EstadoResource(ModelResource):


	class Meta:

		queryset = Area.objects.all()
		resource_name = 'estado'
		authorization = Authorization()
		list_allowed_methods = ['post', 'get']

	def dehydrate(self, bundle):

		nego = int(bundle.request.GET['idne'])
		area = Area.objects.filter(id_negocio_id= nego)
		aux = ""
		for i in area:
			if i.estado == "peligro":
				aux = "Error"
				break
		result = {}
		result['Estado'] = aux
		return result

class ReceiveSensorResource(ModelResource):


	class Meta:
		queryset = Sensor.objects.all()
		resource_name = 'receive'
		authorization= Authorization()
		list_allowed_methods = ['get']

class ReceiveAreaResource(ModelResource):


	class Meta:
		queryset = Area.objects.all()
		resource_name = 'rarea'
		authorization= Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		
		area = Area.objects.all()
		result = {}
		for i in area:
			result['id_area'] = i.id_area
			result['nombre'] = i.nombre
			result['estado'] = i.estado
			result['id_sensor'] = i.id_sensor_id
			result['id_negocio'] = i.id_negocio_id

		return result

class ReceiveNegocioResource(ModelResource):


	class Meta:
		queryset = Negocio.objects.all()
		resource_name = 'rnegocio'
		authorization= Authorization()
		list_allowed_methods = ['get']


class ReceiveEmpleadoResource(ModelResource):


	class Meta:
		queryset = Empleado.objects.all()
		resource_name = 'rempleado'
		authorization= Authorization()
		list_allowed_methods = ['get']

class ReceiveValoresResource(ModelResource):


	class Meta:
		queryset = Valores.objects.all().order_by('-id_valor')
		resource_name = 'rvalor'
		authorization= Authorization()
		list_allowed_methods = ['get']

class ReceiveRelojResource(ModelResource):


	class Meta:
		queryset = Reloj.objects.all()
		resource_name = 'rreloj'
		authorization= Authorization()
		list_allowed_methods = ['get']

class ReceiveHasEmpleadoResource(ModelResource):


	class Meta:
		queryset = HasEmpleado.objects.all()
		resource_name = 'rhasempleado'
		authorization= Authorization()
		list_allowed_methods = ['get']

class ReceiveCredencialResource(ModelResource):


	class Meta:
		queryset = Credencial.objects.all()
		resource_name = 'rcredencial'
		authorization= Authorization()
		list_allowed_methods = ['get']

class ValorEntryResource(ModelResource):


	class Meta:

		queryset = Valores.objects.all().order_by('-id_valor')
		resource_name = 'evalor'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		sensound = eval(bundle.request.GET['sound'])
		senmod = eval(bundle.request.GET['mod'])
		id_sensor = int(bundle.request.GET['ids'])
		sensor = Sensor.objects.filter(id_sensor = id_sensor)[0]
		valor = Valores(sensor_mod = senmod, sensor_sound = sensound, id_sensor = sensor)
		valor.save() 
		

		return bundle

class CredencialCheckResource(ModelResource):


	class Meta:

		queryset = Credencial.objects.all()
		resource_name = 'checre'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		user = str(bundle.request.GET['use'])
		pasw = str(bundle.request.GET['pas'])
		esta = 'OK'	
		result = {}

		credencia = Credencial.objects.filter(username = user)
		if len(credencia) != 0:
			if credencia[0].password != pasw:
				esta = 'Password invalida'
		else:
			esta = 'Username invalido'

		result['Estado'] = esta 
		result['Negocioid'] = 0
		if esta == 'OK':
			hasen = HasEmpleado.objects.filter(id_empleado = credencia[0].id_empleado)[0]
			nego = Negocio.objects.filter(id_negocio = hasen.id_negocio_id)[0]
			result['Negocioid'] = nego.id_negocio
			result['Emergencia'] = nego.telefono
		return result