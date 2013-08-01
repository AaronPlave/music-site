# Create your views here.
# Create your views here.
# from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from Profile.models import Profile

#show email only if logged in, "sign in to contact"

##steps for adding column:
# add thing to model, update admin, views, etc. Then run 
# sqlite3 with the db file, .table to view tables, then
# ALTER TABLE Profile_profile ADD COLUMN (var_name) integer;

def ProfileView(request):
	t = get_template('Profile/Profile.html')
	person = Profile.objects.get(user_id=0)
	user_id,location,email,quote = person.user_id,\
								 person.location, \
								 person.email,\
								 person.quote
	html = t.render(Context({
		'first_name': "Aaron",
		'last_name': "Plave",
		'user_id': user_id,
		'location': location,
		'email':email,
		'quote':quote
		}))
	return HttpResponse(html)

