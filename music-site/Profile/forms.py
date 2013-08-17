from django import forms
from music_site.soundcloud_api import SC_Embed
from Profile.models import *
from django.core import serializers


class EditProfileForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	location = forms.CharField(max_length=30,required=False)
	genres = forms.CharField(widget=forms.Textarea,required=False)
	instruments = forms.CharField(widget=forms.Textarea)
	sc_links = forms.CharField(widget=forms.Textarea,required=False)
	quote = forms.CharField(widget=forms.Textarea, max_length=140,required=False)

	def clean_first_name(self):
		"""
		Django form system knows to look for method whose name
		starts with clean__ and ends with the name of a field. 
		If any such method exists, it's called during validation.
		"""
		first_name = self.cleaned_data['first_name']
		return first_name

	def clean_last_name(self):
		last_name = self.cleaned_data['last_name']
		return last_name

	def clean_location(self):
		location = self.cleaned_data['location']
		return location
	
	def clean_genres(self):
		genres = self.cleaned_data['genres']
		#check for genres, BEST WAY TO REFERENCE DB? OK, maybe have a search bar, 
		# autocomplete/search and select, if not there, OPTION to add, might be typo.
		# maybe have a "did you mean"/include this in the autocomplete 
		genre_list = genres.split()
		db_genres = Genre.objects.values_list('name') #get from db, but cache list
		db_genres = [n[0] for n in db_genres]
		for g in genre_list:
			print g
			if g not in db_genres:
				raise forms.ValidationError(g + "NOT IN DB!")
		return genre_list

	def clean_instruments(self):
		instruments = self.cleaned_data['instruments']

		#check for instruments
		instrument_list = instruments.split()
		db_instruments = Instruments.objects.values_list('name') #get from db, but cache list
		db_instruments = [n[0] for n in db_instruments]
		for g in instrument_list:
			if g not in db_instruments:
				raise forms.ValidationError(g + " NOT IN DB!")
		return instrument_list

	def clean_sc_links(self):
		sc_links = self.cleaned_data['sc_links']
		sc_list = sc_links.split()
		sc = SC_Embed(sc_list)
		if sc[0] == False:
			raise forms.ValidationError(str(sc[1]) + " cannot be processed.")
		return sc_list

	def clean_quote(self):
		quote = self.cleaned_data['quote']
		return quote