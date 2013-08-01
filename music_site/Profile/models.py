from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	# genre_choices = ('Jazz','Classical','Techno','Indie','ETC')
	user_id = models.IntegerField()
	# email = models.EmailField(max_length=75,blank=True)
	# instruments = models.StringListField()
	# genres = models.StringListField()
	location = models.CharField(max_length=35)
	email = models.CharField(max_length=75,blank=True)
	quote = models.TextField(max_length=35)
	# soundcloud_links = models.StringListField()

	def __unicode__(self):
		return self.location
