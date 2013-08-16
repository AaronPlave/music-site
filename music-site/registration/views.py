from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User 
from django.contrib import auth


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")