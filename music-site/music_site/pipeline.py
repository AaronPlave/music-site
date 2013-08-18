from django.http import HttpResponseRedirect
from oauth2 import Token
from social_auth.backends.utils import build_consumer_oauth_request
from social_auth.backends.facebook import FacebookAuth
from social_auth.backends import google

def redirect_to_form(*args, **kwargs):
    if not kwargs['request'].session.get('saved_username') and \
       kwargs.get('user') is None:
        return HttpResponseRedirect('/form/') #just for testing


def username(request, *args, **kwargs):
    if kwargs.get('user'):
        username = kwargs['user'].username
    else:
        username = request.session.get('saved_username')
    return {'username': username}


def redirect_to_form2(*args, **kwargs):
    if not kwargs['request'].session.get('saved_first_name'):
        return HttpResponseRedirect('/form2/') #just for testing


def first_name(request, *args, **kwargs):
    if 'saved_first_name' in request.session:
        user = kwargs['user']
        user.first_name = request.session.get('saved_first_name')
        user.save()
        
def social_profile_image(user,*args, **kwargs):
    provider = kwargs['backend'].name
    print kwargs
    try:
        social_auth = user.social_auth.filter(provider=provider)[0]
    except IndexError:
        print "NO IMAGE"
        return []

    if provider == 'facebook':
        request = "https://graph.facebook.com/me/picture?width=200&access_token=%s" % \
            social_auth.extra_data['access_token']
    # elif provider == 'google':
    #     request =  kwargs['response']
        social_auth.extra_data['profile']  = request
        social_auth.save()
        # print social_auth.extra_data.profile
        print request

def new_user_check(user,*args,**kwargs):
    print args,kwargs,user
    print kwargs['new_association']
    if kwargs['new_association'] == True:
        return HttpResponseRedirect('/create_profile/')