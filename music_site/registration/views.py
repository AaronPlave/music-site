from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User 
from django.contrib import auth


def SignupView(request,username='',first_name='',last_name='',
				password='',verify_pass='',email=''):
	t = get_template('Auth/signup.html')
	html = t.render(Context({
		'username': username,
		'first_name': first_name,
		'last_name':last_name,
		'password': password,
		'verify_pass': verify_pass,
		'email': email
		}))
	return HttpResponse(html)

def LoginView(request,username='',password=''):
	t = get_template('Auth/login.html')
	html = t.render(Context({
		'username':username,
		'password':password
		}))
	return HttpResponse(html)