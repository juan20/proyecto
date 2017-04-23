from tastypie.resources import ModelResource,Resource
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
import time
from tastypie import fields
from main.models import *

class EntryResource(ModelResource):
     

	class Meta:
		queryset = Information.objects.all()
        resource_name = 'entry'
        authorization= Authorization()
        list_allowed_methods = ['get']

	


	def dehydrate(self,bundle):

		date = str(bundle.request.GET['dat'])
		sensor_sound = int(bundle.request.GET['sound'])
		sensor_mod = bool(bundle.request.GET['mod'])
		
		
		info = Information(date = date,sensor_mod = sensor_mod,sensor_sound = sensor_sound)
		info.save()
		
		return "SAVED"
		
class ReceiveResource(ModelResource):
     

	class Meta:
		queryset = Information.objects.all().order_by('-id_information')
        resource_name = 'receive'
        authorization= Authorization()
        list_allowed_methods = ['get']
