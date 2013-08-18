# Create your views here.
# Create your views here.
# from django.http import HttpResponseRedirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from Profile.models import Profile, Genre, Instruments
from Profile.models import SoundCloud as SC
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from Profile.forms import EditProfileForm
from music_site.soundcloud_api import SC_Embed
import json
from django.shortcuts import render

#show email only if logged in, "sign in to contact"

##steps for adding column:
# add thing to model, update admin, views, etc. Then run 
# sqlite3 with the db file, .table to view tables, then
# ALTER TABLE Profile_profile ADD COLUMN (var_name) integer;

def ProfileView(request,pk):
	# t = get_template('Profile/Profile.html')

	##GET THIS FROM USER LOGIN ID

	#get username/id/whatever from request
	user = User.objects.filter(pk=pk)[0]
	person = Profile.objects.filter(User=user)[0]
	genres = person.genre.all()
	instruments = person.instruments.all()
	sc_urls = person.soundcloud_set.all()
	embed_lst = [i.html for i in sc_urls]

	print request.user.is_authenticated()
	print embed_lst,"w"

	#Check if user is owner of this Profile
	if request.user.is_authenticated():
		print user.email,request.user.email
		if user.email == request.user.email:
			print "same"
			request.user.owner = True

			#grab profile picture, if not, default image
			provider = request.session['social_auth_last_login_backend']
			print provider
			picture =  request.user.social_auth.get(provider=provider).extra_data['profile']

	return render(request,"Profile/Profile.html",{
		'first_name': user.first_name,
		'last_name': user.last_name,
		'location': person.location,
		'genres': genres,
		'instruments':instruments,
		'quote':person.quote,
		'soundcloud':embed_lst,
		'pk':pk,
		'picture_url':picture,
	})

def EditProfileView(request,pk): #secure way to do this?
	user = User.objects.filter(pk=pk)[0]
	person = Profile.objects.filter(User=user)[0]

	genre_list = person.genre.values_list('name')
	genre_str = "\n".join([i[0] for i in genre_list])

	instrument_list = person.instruments.values_list('name')
	instrument_str = "\n".join([i[0] for i in instrument_list])

	sc_list = person.soundcloud_set.values_list('url')
	sc_str = "\n".join([i[0] for i in sc_list])
	
	data_dict = {"genre_list":genre_list,
				 "instrument_list":instrument_list,
				 "sc_list":sc_list,
				 "person":person,
				 "new":False,
				}

	embed_lst = SC_Embed(sc_list)[1]
	#form checking
	errors = []
	if request.method == 'POST':
		print "POST"
		form = EditProfileForm(request.POST,data_dict=data_dict)
		if form.is_valid():
			cd = form.cleaned_data

			user.first_name = cd['first_name']
			user.last_name = cd['last_name']
			person.location = cd['location']

			genre_models = [Genre.objects.filter(name=i)[0] for i in cd['genres']] #MUST BE A BETTER WAY!!!?? DON'T WANT TO HIT DB EVERY TIME FOR THIS...
			person.genre = genre_models

			instruments_models = [Instruments.objects.filter(name=i)[0] for i in cd['instruments']]
			person.instruments = instruments_models

			sc_dict = cd['sc_links']
			if sc_dict:
				sc_models = [SC.objects.create(url=i,owner_id=person.pk,html=sc_dict[i]) for i in sc_dict.keys()]
			# print sc_models,"HI"
			# print person.soundcloud_set,person.soundcloud_set.all()
				person.soundcloud_set = sc_models

				person.quote = cd['quote']
				user.save()
				person.save()

			return HttpResponseRedirect('/profile/'+str(pk))
		else:
			print "no"
	else:
		form = EditProfileForm(data_dict=data_dict,
			initial={'first_name': user.first_name,
					'last_name': user.last_name,
					'location': person.location,
					'genres': genre_str,
					'instruments':instrument_str,
					'quote':person.quote,
					'sc_links':sc_str,}) #init fields, grab from db, from cache later
	return render_to_response('Profile/EditProfile.html',{'form':form},
							context_instance=RequestContext(request))


	# 	return redirect('/profile/'+str(pk))
	# t = get_template('Profile/EditProfile.html')
	# html = t.render(Context())
	# return render_to_response('Profile/EditProfile.html', {}, RequestContext(request))

def form2(request):
	if request.method == 'POST' and request.POST.get('first_name'):
	    request.session['saved_first_name'] = request.POST['first_name']
	    name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
	    backend = request.session[name]['backend']
	    return redirect('socialauth_complete', backend=backend)
	return render_to_response('home/form2.html', {}, RequestContext(request))

