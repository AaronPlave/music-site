# Create your models here.
from django.db import models

class Temp_User(models.Model):
	"""Temporary user shit until I figr out the real deal"""
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=75
)	# NEED PROFILE IMAGE WITH REAL DEAL IF POSSIBLE

	def __unicode__(self):
		return self.first_name