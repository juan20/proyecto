from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Information(models.Model):
    
    id_information = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    sensor_mod = models.BooleanField(default=False)
    sensor_sound = models.BooleanField(default=False)
	
