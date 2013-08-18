from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User 
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from Profile.models import Profile, Genre, Instruments, SoundCloud
from Profile.forms import EditProfileForm
from django.template import RequestContext




def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def CreateUserView(request):
	user = request.user
	if not user.is_authenticated():
		return HttpResponseRedirect("/")

	data_dict = {'new':True}

	#create new profile for user
	errors = []
	if request.method == 'POST':
		print "POST"
		form = EditProfileForm(request.POST,data_dict=data_dict)
		print form
		if form.is_valid():
			try: #to catch primary key errors if profile already exists
				person = Profile.objects.create(User=user)
			except:
				return HttpResponseRedirect("/profile/"+str(user.pk)) #problem with "last login backend", deal with it, need provider..
			
			print "valid form"
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
				sc_models = [SoundCloud.objects.create(url=i,owner_id=person.pk,html=sc_dict[i]) for i in sc_dict.keys()]
				person.soundcloud_set = sc_models

				person.quote = cd['quote']
				user.save()
				person.save()

			return HttpResponseRedirect('/profile/'+str(person.pk))
		else:
			print "no"
	else:
		form = EditProfileForm(data_dict=data_dict,
			initial={'first_name': user.first_name,
					'last_name': user.last_name,
					'location': "",
					'genres': "",
					'instruments':"",
					'quote':"",
					'soundcloud':"",}) #init fields, grab from db, from cache later
	return render_to_response('registration/CreateUser.html',{'form':form},
							context_instance=RequestContext(request))