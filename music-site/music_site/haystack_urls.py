from django.conf.urls.defaults import *
from haystack.views import SearchView
from haystack.query import SearchQuerySet

sqs = SearchQuerySet().order_by('instruments')

urlpatterns = patterns('haystack.views',
    url(r'^$', SearchView(searchqueryset=sqs),name='haystack_search'), 
)