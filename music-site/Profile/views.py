# Create your views here.
# Create your views here.
# from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from Profile.models import Profile, Genre, Instruments
from Profile.models import SoundCloud as SC
from registration.models import Temp_User

import soundcloud

#show email only if logged in, "sign in to contact"

##steps for adding column:
# add thing to model, update admin, views, etc. Then run 
# sqlite3 with the db file, .table to view tables, then
# ALTER TABLE Profile_profile ADD COLUMN (var_name) integer;

def ProfileView(request,pk):
	t = get_template('Profile/Profile.html')

	##GET THIS FROM USER LOGIN ID
	
	#grabs first user in location
	p = Profile
	person = p.objects.filter(location='Wesleyan')[0]

	#grabs by User by first_name!!!
	#get username/id/whatever from request
	user = Temp_User.objects.filter(pk=pk)[0]
	person = Profile.objects.filter(User=user)[0]
	genres = person.genre.all()
	instruments = person.instruments.all()
	sc_urls = person.soundcloud_set.all()
	embed_lst = SC_Embed(sc_urls)
	# User,location = person.User,person,location

	html = t.render(Context({
		'first_name': user.first_name,
		'last_name': user.last_name,
		'location': person.location,
		'genres': genres,
		'instruments':instruments,
		'quote':person.quote,
		'soundcloud':embed_lst,
		}))
	return HttpResponse(html)

def EditProfileView(request):
	t = get_template('Profile/EditProfile.html')
	html = t.render(Context())
	return HttpResponse(html)

def SC_Embed(url_lst):
	client = soundcloud.Client(client_id="858c98ac9ee828617aa6a2364d5b0b0a")
	embed_lst = []
	for link in url_lst:
		track_url = client.get('/resolve',url=link)
		embed_info = client.get('/oembed',url=track_url.url)
		embed_lst.append(embed_info.html)
	return embed_lst
