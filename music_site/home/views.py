# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from Profile.models import Profile


# class HomeView(generic.DetailView):
#     template_name = 'home/home.html'

def HomeView(request):
	t = get_template('home/home.html')
	html = t.render(Context())
	return HttpResponse(html)

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