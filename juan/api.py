from tastypie.resources import ModelResource,Resource
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
import time
from tastypie import fields, utils

from main.models import *
from datetime import datetime
import pyrebase

#Definicion de la funcion que deben de ejecutar cada vez que se actualice uno de los valores
def addLog(id, nombre, estadomov, estadoson):
    fecha_actual = time.strftime("%d/%m/%Y")
    data = {"id": id , "nombre":nombre, "estadomov":estadomov, "estadoson":estadoson, "fecha":fecha_actual}
    db.child("Data").push(data)
    print("Data enviada...")


config = {
  "apiKey": "AIzaSyCHmb3CoBZwJO9hcPgZjKsHH9W18u2Pcd0",
  "authDomain": "jjsecurity-600f1.firebaseapp.com",
  "databaseURL": "https://jjsecurity-600f1.firebaseio.com",
  "storageBucket": "jjsecurity-600f1.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


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
		resource_name = 'sarea'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		are = int(bundle.request.GET['sa'])
		estad = str(bundle.request.GET['est'])
		area = Area.objects.filter(id_area = are)[0]
		sensor = Sensor.objects.filter(id_sensor = area.id_sensor_id)[0]
		valor = Valores(sensor_mod = False, sensor_sound = False, id_sensor = sensor.id_sensor)
		addLog(str(sensor),'UNKNOW',str(senmod),str(sensound))
		valor.save()
		area.estado = estad
		area.save() 

		return area.estado


class EstadoResource(ModelResource):


	class Meta:

		queryset = Area.objects.all()
		resource_name = 'estado'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		nego = int(bundle.request.GET['idne'])
		area = Area.objects.filter(id_negocio_id= nego)
		aux = "OK"
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
		authorization = Authorization()
		list_allowed_methods = ['get']

class ReceiveAreaResource(ModelResource):


	class Meta:
		queryset = Area.objects.all()
		resource_name = 'rarea'
		authorization = Authorization()
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
		addLog(str(sensor),'UNKNOW',str(senmod),str(sensound))
		valor.save()
		
		return bundle

class ValorAEntryResource(ModelResource):


	class Meta:

		queryset = Valores.objects.all().order_by('-id_valor')
		resource_name = 'eavalor'
		authorization = Authorization()
		list_allowed_methods = ['get']

	def dehydrate(self, bundle):

		sensound = eval(bundle.request.GET['sound'])
		senmod = eval(bundle.request.GET['mod'])
		id_area = int(bundle.request.GET['ida'])
		area = Area.objects.filter(id_area = id_area)[0]
		sensor = Sensor.objects.filter(id_sensor = area.id_sensor_id)[0]
		valor = Valores(sensor_mod = senmod_id, sensor_sound = sensound, id_sensor = sensor)
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
			result['Emergencia'] = 'tel:'+ nego.telefono
		return result

class NegocioTotal(ModelResource):


	class Meta:

		queryset = Negocio.objects.all()
		resource_name = 'negid'
		authorization = Authorization()
		list_allowed_methods = [ 'get']

	def dehydrate(self, bundle):

		nego = int(bundle.request.GET['idne'])
		hasemp = HasEmpleado.objects.filter(id_negocio_id = nego)
		areas = Area.objects.filter(id_negocio_id = nego)
		result = []
		print ("hasemp klk")
		print (hasemp)
		for i in hasemp:

			has = {}
			has['id_hasempleado'] = i.id_hasEmpleado
			has['id_empleado'] = i.id_empleado
			emp = Empleado.objects.filter(id_empleado = i.id_empleado_id)[0]
			has['nombre_empleado'] = emp.nombre
			has['direccion_empleado'] = emp.direccion
			has['telefono_empleado'] = emp.telefono
			has['flota_empleado'] = emp.flota
			cre = Credencial.objects.filter(id_empleado = i.id_empleado_id)[0]
			has['id_credencial'] = cre.id_crendencial
			has['user_credencial'] = cre.username
			has['password_credencial'] = cre.password
			result.append(has)
			
		for ia in areas:
			are = {}
			are['id_area'] = ia.id_area
			are['nomre_area'] = ia.nombre
			are['estado_area'] = ia.estado
			sen = Sensor.objects.filter(id_sensor = ia.id_sensor_id)[0]
			are['id_sensor_area']= sen.id_sensor
			are['estado_sensor'] = sen.estado
			val = Valores.objects.filter(id_sensor = sen.id_sensor)
			print("total valore: ")
			print(len(val))
			print(val)
			print("ultimo valor: ")
			print(val[len(val)-1])
			data= []
			for iva in val:
				valo= {}
				valo['id_valor'] = iva.id_valor
				valo['date'] = iva.date
				valo['sensor_mod'] = iva.sensor_mod
				valo['sensor_sound'] = iva.sensor_sound
				data.append(valo)
			are['valores'] = data
			result.append(are)
		
		return result