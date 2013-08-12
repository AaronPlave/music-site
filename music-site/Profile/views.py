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

#show email only if logged in, "sign in to contact"

##steps for adding column:
# add thing to model, update admin, views, etc. Then run 
# sqlite3 with the db file, .table to view tables, then
# ALTER TABLE Profile_profile ADD COLUMN (var_name) integer;

def ProfileView(request,pk):
	t = get_template('Profile/Profile.html')

	##GET THIS FROM USER LOGIN ID
	
	#grabs first user in location
	# p = Profile
	# person = p.objects.filter(location='Wesleyan')[0]

	#grabs by User by first_name!!!
	#get username/id/whatever from request
	user = User.objects.filter(pk=pk)[0]
	person = Profile.objects.filter(User=user)[0]
	genres = person.genre.all()
	instruments = person.instruments.all()
	sc_urls = person.soundcloud_set.all()
	embed_lst = SC_Embed(sc_urls)[1] #DEFINITELY CACHE THIS
	# User,location = person.User,person,location

	html = t.render(Context({
		'first_name': user.first_name,
		'last_name': user.last_name,
		'location': person.location,
		'genres': genres,
		'instruments':instruments,
		'quote':person.quote,
		'soundcloud':embed_lst,
		'pk':pk,
		}))
	return HttpResponse(html)

def EditProfileView(request,pk): #secure way to do this?
	user = User.objects.filter(pk=pk)[0]
	person = Profile.objects.filter(User=user)[0]
	genres = person.genre.all()
	instruments = person.instruments.all()
	sc_urls = person.soundcloud_set.all()
	embed_lst = SC_Embed(sc_urls)[1]
	#form checking
	errors = []
	if request.method == 'POST':
		print "POST"
		form = EditProfileForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print cd
			#NOW UPDATE PROFILE DATABASE

			user.first_name = cd['first_name']
			user.last_name = cd['last_name']
			person.location = cd['location']
			print person.genre.all()
			# person.genre = cd['genres'] #hmm.. might not work
			# person.instruments = cd['instruments']
			# person.soundcloud_set = cd['sc_links']
			person.quote = cd['quote']
			user.save()
			person.save()

			return HttpResponseRedirect('/profile/'+str(pk))
		else:
			print "no"
	else:
		#these next two lines are quite silly, i'm sure there's a way to do this
		genre_list = [str(g.name) for g in genres]
		instrument_list = [str(i.name) for i in instruments]
		form = EditProfileForm(
			initial={'first_name': user.first_name,
					'last_name': user.last_name,
					'location': person.location,
					'genres': genre_list,
					'instruments':instrument_list,
					'quote':person.quote,
					'soundcloud':embed_lst,}) #init fields, grab from db, from cache later
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

