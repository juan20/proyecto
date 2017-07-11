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
