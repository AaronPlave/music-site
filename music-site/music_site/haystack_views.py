from haystack.query import SearchQuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.mail import send_mail

from django.template.loader import get_template
from django.template import Context
from Profile.models import Profile
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from home.forms import ContactForm

from django.http import HttpResponseRedirect

def SearchViewSort(request,sort_option=False):
	"""Landing page for search results"""

	#characters in search field
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		t = get_template('home/results.html')
		
		if len(q) > 30:
			message = "Search query too long, try a shorter query."
			return HttpResponse(message)

			
		#Obviously make this search better
		results = Profile.objects.filter(location__icontains=q)
		html = t.render(Context({'results':results,'query':q}))
		return HttpResponse(html)

	#in case of blank search
	elif 'q' in request.GET:
		results = Profile.objects.all()
		q = "Here's everything, you scoundrel."
		t = get_template('home/results.html')
		html = t.render(Context({'results':results,'query':q}))
		return HttpResponse(html)

	#navigating to the /results/ page
	else:
		message = 'This page ain\'t big enough for the one of you, so gerroff\' this page'
		return HttpResponse(message)

	sqs = SearchQuerySet().all()
	
	sqs = sqs.order_by('location')

	return HttpResponse(sqs)
