from tastypie.resources import ModelResource,Resource
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
import time
from tastypie import fields
from main.models import *

class ModulosResource(ModelResource):


	class Meta:

		queryset = Area.objects.all()
		resource_name = 'modulo'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		negocio = int(bundle.request.GET['idne'])
		area = Area.objects.filter(id_negocio = negocio)
		result = {}
		result['modulos'] = []

		for i in area:
			aux = {}
			aux ['id'] = area.id_area
			aux ['nombre'] = area.nombre
			aux ['estado'] = area.estado
			result['modulos'].append(aux)


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
		sensores = Area.objects.filter(id_negocio = negocio)
		result['sensores'] = len(sensores)
		result['servidores'] = 2



		return result

class AreaResource(ModelResource):


	class Meta:

		queryset = Area.objects.all()
		resource_name = 'area'
		authorization = Authorization()
		list_allowed_methods = ['post']

	def dehydrate(self, bundle):

		area = int(bundle.request.GET['ida'])
		estad = str(bundle.request.GET['est'])
		Area.objects.filter(id_area = area)[0] = estad
		Area.estado = estad
		result = {}
		result['Estado'] = estad
		return result


class EstadoResource(ModelResource):


	class Meta:

		queryset = Area.objects.all()
		resource_name = 'estado'
		authorization = Authorization()
		list_allowed_methods = ['post']

	def dehydrate(self, bundle):

		nego = int(bundle.request.GET['idne'])
		area = Area.filter(id_negocio= nego)
		aux = ""
		for i in area:
			if area.estado == "peligro":
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
		queryset = Valores.objects.all()
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
		resource_name = 'rhasempleado'
		authorization= Authorization()
		list_allowed_methods = ['get']
