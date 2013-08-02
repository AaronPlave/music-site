from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

# from Auth import views as Auth_views
from registration.views import LoginView, SignupView #LogoutView

#search results
from home.views import ResultsView, ContactView, AboutView

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

    url(r'^login/$', LoginView),

    # url(r'^logout/$',LogoutView),

    url(r'^signup/$',SignupView),

    url(r'^contact/$',ContactView),

    url(r'^results/$',ResultsView),

    url(r'^about/$', AboutView),

    url(r'^accounts/login/$', login),

    url(r'^accounts/logout/$',logout),

    url(r'', include('social_auth.urls')),
    
)
