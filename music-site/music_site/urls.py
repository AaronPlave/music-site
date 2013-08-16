from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

# from Auth import views as Auth_views
from registration.views import logout_view

#search results
from home.views import ResultsView, ContactView, AboutView, BaseView

#used in social-auth
from django.views.generic import RedirectView

from home.views import form,form2

from music_site import haystack_urls




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music_site.views.home', name='home'),
    # url(r'^music_site/', include('music_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Adding namespace here to tell Django which app view to create for 
    #a url when using the {%url% template}
    # url(r'^polls/', include('polls.urls',namespace="polls")),


    #home page for search + login + signup + about, serve that index page.
    url(r'^',include('home.urls',namespace="home")),

    #home page for profile
    url(r'^profile/',include('Profile.urls',namespace="Profile")),

    # url(r'^signup/',Auth_views.SignupView), #HAVE TO LIMIT TO ONE, OTHERWISE /signup/signup/signup works! 
    
    # url(r'^login/',Auth_views.LoginView),

    # url(r'^login/$', RedirectView.as_view(url='/login/facebook/')),

    # url(r'^logout/$',LogoutView),

    # url(r'^signup/$',SignupView),

    url(r'^contact/$',ContactView),

    url(r'^results/$',ResultsView),

    url(r'^about/$', AboutView),

    #for every service you use, the login/**** is what you go to for our app to know which service to use
    # url(r'^login/$', redirect_to, {'url':'/login/github'}), 

    url(r'^accounts/logout/$',logout_view),

    url(r'', include('social_auth.urls')),
    url(r'^form2/$', form2, name='form2'),
    url(r'^form/$', form, name='form'),
    url(r'^base/$',BaseView),
    # url(r'^search/', include('music_site.haystack_urls')),
    url(r'^search/$', include(haystack_urls)),
    
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()