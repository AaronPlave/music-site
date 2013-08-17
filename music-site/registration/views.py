from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User 
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from Profile.models import Profile, Genre, Instruments


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def CreateUserView(request):
	u = request.user

	# check to see if the user already exists, if so redirect elsewhere
	# recheck to ensure user is first time user

	#create new profile for user

	print u
	return render_to_response('registration/CreateUser.html')