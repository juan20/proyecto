from tastypie.resources import ModelResource,Resource
from tastypie.authorization import Authorization
from tastypie.constants import ALL
import time
from tastypie import fields
from main.models import *
import urllib3,ast,re

class SaveDatabase(ModelResource):
     

	class Meta:
		queryset = Information.objects.all()
		resource_name = 'save'
		limit = 0
		authorization= Authorization()
		list_allowed_methods = ['post']


	def dehydrate(self,bundle):

		begintime = str(bundle.request.GET['begintime'])
		endtime = str(bundle.request.GET['endtime'])
		budget = int(bundle.request.GET['limit'])
		city = bundle.request.GET['city']
		preferences = re.split('[\[,\,,\',\]]',bundle.request.GET['preferences'])
		while '' in preferences: preferences.remove('')
		result = createOffersToUser(datetime.datetime.strptime(begintime,"%Y-%m-%d %H:%M:%S"), datetime.datetime.strptime(endtime,"%Y-%m-%d %H:%M:%S"),budget,Tblcity.objects.get(cityname = city),preferences,{"Adult":1})

		return result