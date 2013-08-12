# Create your views here.
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
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages

from social_auth import __version__ as version
from social_auth.utils import setting


# class HomeView(generic.DetailView):
#     template_name = 'home/home.html'

def HomeView(request):
	t = get_template('home/home.html')
	html = t.render(Context())
	return HttpResponse(html)

def BaseView(request):
	t = get_template('home/base.html')
	html = t.render(Context())
	return HttpResponse(html)


def AboutView(request):
	t = get_template('home/about.html')
	html = t.render(Context())
	return HttpResponse(html)

def ContactView(request):

	#The c is for csrf stuff 
	# c = {}
	# c.update(csrf(request))
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data

			#CONFIGURE MAIL SERVER LATER
			# send_mail(
   #              cd['subject'],
   #              cd['message'],
   #              cd.get('email', 'noreply@example.com'),
   #              ['siteowner@example.com'],
   #          )
			return HttpResponseRedirect('/')
	else:
		form = ContactForm(
			initial={'subject':'Ask me your questions three'}) #init message
		t = get_template('home/contact.html')
	return render_to_response('home/contact.html',{'form':form},
								context_instance=RequestContext(request))

def ResultsView(request):
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

#stick this in results for error handling if ye (me) want(s).
# {% if error %}
#         <p style="color: red;">Please submit a search term.</p>
#     {% endif %}


def form2(request):
	if request.method == 'POST' and request.POST.get('first_name'):
	    request.session['saved_first_name'] = request.POST['first_name']
	    name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
	    backend = request.session[name]['backend']
	    return redirect('socialauth_complete', backend=backend)
	return render_to_response('home/form2.html', {}, RequestContext(request))