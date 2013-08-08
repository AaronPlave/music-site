"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from registration.models import Temp_User
from Profile.models import Profile,Genre,SoundCloud,Instruments
import csv

class Populate_DB():
    def Pop_DB(self):
        """
        Populates User and Profile DBs.
        """
        fields = ['first_name','last_name','email']
        for row in csv.reader(open('/home/aaron/music_site_git/music_site/music_site/User_DB.csv')):
        	Temp_User.objects.create(**dict(zip(fields,row)))

        fields = ['name']
        for row in csv.reader(open('/home/aaron/music_site_git/music_site/music_site/Genre_DB.csv')):
        	Genre.objects.create(**dict(zip(fields,row)))

        # fields = ['url']
        # for row in csv.reader(open('/home/aaron/music_site_git/music_site/music_site/SoundCloud_DB.csv')):
        # 	SoundCloud.objects.create(**dict(zip(fields,row)))

        fields = ['name']
        for row in csv.reader(open('/home/aaron/music_site_git/music_site/music_site/Instruments_DB.csv')):
        	Instruments.objects.create(**dict(zip(fields,row)))