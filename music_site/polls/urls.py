from django.conf.urls import patterns, url

from polls import views



#If you want to change the URL of the polls detail view to something else, 
#perhaps to something like polls/specifics/12/ instead of doing it in the 
#template (or templates) you would change it in polls/urls.py:

urlpatterns = patterns('',
	#ex: /polls/
	url(r'^$',views.IndexView.as_view(),name='index'),

	#ex: /polls/5/
	# the 'name' value as called by the {% url %} template tag
	url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='detail'),

	#ex: /polls/5/results/
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),

	#ex: /polls/5/vote/
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)

