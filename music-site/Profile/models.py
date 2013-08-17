from django.db import models
# from registration.models import Temp_User
from django.contrib.auth.models import User


#ID link to Users DB is created when you create the profile, 
# say that p = Profile(first_name=INSERT-USER-ID-HERE, location,..) 

class Genre(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return unicode(self.name)

	def __str__(self):
		return str(self.name)

class SoundCloud(models.Model):
	#Assumes all urls are valid
	url = models.CharField(max_length=300)
	owner = models.ForeignKey('Profile')

	def __unicode__(self):
		return unicode(self.url)

class Instruments(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return unicode(self.name)
		
	def __str__(self):
		return str(self.name)

class Profile(models.Model):

	#User gives first, last name, real email(?)
	User = models.OneToOneField(User,primary_key=True)
	genre = models.ManyToManyField(Genre)
	instruments = models.ManyToManyField(Instruments)
	location = models.CharField(max_length=35)
	quote = models.TextField(max_length=140)

	def __unicode__(self):
		return unicode(self.User)

