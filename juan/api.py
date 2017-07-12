from tastypie.resources import ModelResource,Resource
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
import time
from tastypie import fields
from main.models import *

class InformationEntryResource(ModelResource):


	class Meta:

		queryset = Information.objects.all()
		resource_name = 'entry'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		date = str(bundle.request.GET['dat'])
		sensor_sound = int(bundle.request.GET['sound'])
		sensor_mod = bool(bundle.request.GET['mod'])
		mac = str(bundle.request.GET['mc'])
		id_empresa = str(bundle.request.GET['ide'])
		
		mac_obj = Xbee.objects.filter(mac=mac)[0]
		empresa_obj = Empresa.objects.filter(nombre=id_empresa)[0]
		
		info = Information(date = date, sensor_mod = sensor_mod, sensor_sound = sensor_sound, mac = mac_obj, id_empresa = empresa_obj)
		info.save()

		return bundle

class XbeeEntryResource(ModelResource):

	class Meta:

		queryset = Xbee.objects.all()
		resource_name = 'xbee'
		authorization = Authorization()
		list_allowed_methods = ['get']


	def dehydrate(self, bundle):

		mac = str(bundle.request.GET['mc'])
		red = str(bundle.request.GET['net'])
		tipo = str(bundle.request.GET['tip'])
		
		xb = Xbee(mac = mac, red = red, tipo = tipo)
		xb.save()

		return bundle

class UsuarioEntryResource(ModelResource):


	class Meta:

		queryset = usuario.objects.all()
		resource_name = 'usuario'
		authorization = Authorization()
		list_allowed_methods = ['get']


	def dehydrate(self, bundle):

		nombre = str(bundle.request.GET['name'])
		apellido = str(bundle.request.GET['last'])
		usuar = str(bundle.request.GET['use'])
		priv = int(bundle.request.GET['pri'])
		passw = str(bundle.request.GET['pas'])
		id_empresa = int(bundle.request.GET['ide'])
		empresa_obj = Empresa.objects.filter(nombre=id_empresa)[0]
		
		user = usuario(nombre = nombre, apellido = apellido, username = usuar, privilegio = privilegio, password = passw, id_empresa = empresa_obj)
		user.save()

		return bundle
		
class UserResource(ModelResource):


	class Meta:

		queryset = usuario.objects.all()
		resource_name = 'user'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		user = str(bundle.request.GET['usr'])
		pasw = int(bundle.request.GET['pasw'])
		usr = usuario.objects.filter(username = user, password = pasw)[0]
		result = {}
		result['nombre'] = usr.nombre
		result['apellido'] = usr.apellido
		result['privilegio'] = usr.privilegio
		result['xbees'] = []
		result['informations'] = []

		if usr.privilegio == 3:
			
			result['empresas'] = []

			for i in Empresa.objects.all():
				result['empresas'].append(i.__dict__)
			for i in Xbee.objects.all():
				result['xbees'].append(i.__dict__)
			for i in Information.objects.all():
				result['informations'].append(i.__dict__)
		else:

			result['empresa'] = usr.id_empresa.nombre

			for i in Information.objects.filter(id_empresa = usr.id_empresa.id_empresa):
				result['informations'] = i.__dict__
				mac = Xbee.objects.filter(mac = i.mac)
				
				if mac.__dict__ not in result['xbees']:
					result['xbees'].append(mac.__dict__)
		

		return result


class EmpresaEntryResource(ModelResource):


	class Meta:

		queryset = Empresa.objects.all()
		resource_name = 'empresa'
		authorization = Authorization()
		list_allowed_methods = ['get']


	def dehydrate(self, bundle):

		nombre = str(bundle.request.GET['name'])
		cant = int(bundle.request.GET['can'])		
		emp = Empresa(nombre = nombre, cantidad_usuarios = cantidad_usuarios)
		emp.save()

		return bundle

class ReceiveResource(ModelResource):


	class Meta:
		queryset = Information.objects.all().order_by('-id_information')
		resource_name = 'receive'
		authorization= Authorization()
		list_allowed_methods = ['get']
