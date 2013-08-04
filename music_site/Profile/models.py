from django.db import models
from registration.models import Temp_User


#ID link to Users DB is created when you create the profile, 
# say that p = Profile(first_name=INSERT-USER-ID-HERE, location,..) 

class Genre(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return unicode(self.name)

class Profile(models.Model): #CARS
	# genre_choices = ('Jazz','Classical','Techno','Indie','ETC')
	# Person = models.CharField(max_length=30) #what do I name this?
	User = models.OneToOneField(Temp_User,primary_key=True)
	genre = models.ManyToManyField(Genre)

	# instruments = models.StringListField()
	# genres = models.StringListField()
	location = models.CharField(max_length=35)
	# email = models.CharField(max_length=75,blank=True)
	# quote = models.TextField(max_length=140)
	# soundcloud_links=  models.StringListField()

	def __unicode__(self):
		return unicode(self.User)

