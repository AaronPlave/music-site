from django.conf.urls import *
from music_site.haystack_views import basic_search
from haystack.query import SearchQuerySet


# sqs = SearchQuerySet().filter(content__startswith='examp')
# sqs = sqs.filter(content__contains='examp'))

urlpatterns = patterns('haystack.views',
    url(r'^$', basic_search,name='haystack_search'), 
)