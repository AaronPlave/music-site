# Create your views here.
# Create your views here.
# from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from Profile.models import Profile, Genre
from registration.models import Temp_User

import soundcloud

#show email only if logged in, "sign in to contact"

##steps for adding column:
# add thing to model, update admin, views, etc. Then run 
# sqlite3 with the db file, .table to view tables, then
# ALTER TABLE Profile_profile ADD COLUMN (var_name) integer;

def ProfileView(request):
	t = get_template('Profile/Profile.html')

	##GET THIS FROM USER LOGIN ID
	
	#grabs first user in location
	p = Profile
	person = p.objects.filter(location='Wesleyan')[0]

	#grabs by User by first_name!!!
	#get username/id/whatever from request
	name = "Aaron"
	user = Temp_User.objects.filter(first_name=name)[0]
	person = Profile.objects.filter(User=user)[0]
	genres = person.genre.all()
	soundcloud_embed = SoundCloud('https://soundcloud.com/serious-url/cut-to-black-1')
	print soundcloud_embed
	# User,location = person.User,person,location

	html = t.render(Context({
		'first_name': user.first_name,
		'last_name': user.last_name,
		'location': person.location,
		'genres': genres,
		'quote':"quote",
		'soundcloud':soundcloud_embed,
		}))
	return HttpResponse(html)

def EditProfileView(request):
	t = get_template('Profile/EditProfile.html')
	html = t.render(Context())
	return HttpResponse(html)

def SoundCloud(plain_url):
	client = soundcloud.Client(client_id="858c98ac9ee828617aa6a2364d5b0b0a")
	track_url = client.get('/resolve',url='https://soundcloud.com/serious-url/cut-to-black-1')
	embed_info = client.get('/oembed',url=track_url.url)
	print embed_info.html
	return embed_info.html
