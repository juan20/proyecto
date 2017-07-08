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
		id_empresa = int(bundle.request.GET['ide'])
		
		info = Information(date = date, sensor_mod = sensor_mod, sensor_sound = sensor_sound, mac= mac, id_empresa= id_empresa)
		info.save()

		return super(InformationEntryResource, self).save(*args, **kwargs)

class XbeeEntryResource(ModelResource):


	class Meta:

		queryset = Xbee.objects.all()
		resource_name = 'entry'
		authorization = Authorization()
		list_allowed_methods = ['get']

	


	def dehydrate(self, bundle):

		mac = str(bundle.request.GET['mc'])
		red = str(bundle.request.GET['net'])
		tipo = str(bundle.request.GET['tip'])
		
		
		xb = Xbee(mac = mac, red = red, tipo = tipo)
		xb.save()

		return super(XbeeEntryResource, self).save(*args, **kwargs)

class UsuarioEntryResource(ModelResource):


	class Meta:

		queryset = usuario.objects.all()
		resource_name = 'entry'
		authorization = Authorization()
		list_allowed_methods = ['get']

	


	def dehydrate(self, bundle):

		nombre = str(bundle.request.GET['name'])
		apellido = str(bundle.request.GET['last'])
		usuar = str(bundle.request.GET['use'])
		priv = int(bundle.request.GET['pri'])
		passw = str(bundle.request.GET['pas'])
		id_empresa = int(bundle.request.GET['ide'])
		
		user = usuario(nombre = nombre, apellido = apellido, usuar = usuario, priv = privilegio, passw = password, id_empresa= id_empresa)
		user.save()

		return super(UsuarioEntryResource, self).save(*args, **kwargs)

class EmpresaEntryResource(ModelResource):


	class Meta:

		queryset = Empresa.objects.all()
		resource_name = 'entry'
		authorization = Authorization()
		list_allowed_methods = ['get']

	


	def dehydrate(self, bundle):

		nombre = str(bundle.request.GET['name'])
		cant = int(bundle.request.GET['can'])
		
		
		
		emp = Empresa(nombre = nombre, cant = cantidad_usuarios)
		emp.save()

		return super(EmpresaEntryResource, self).save(*args, **kwargs)
		
class ReceiveResource(ModelResource):


	class Meta:
		queryset = Information.objects.all().order_by('-id_information')
		resource_name = 'receive'
		authorization= Authorization()
		list_allowed_methods = ['get']
