from django import forms
from music_site.soundcloud_api import SC_Embed
from Profile.models import *
from django.core import serializers


class EditProfileForm(forms.Form):
	def __init__(self,*args,**kwargs):
		print 
		self.data_dict = kwargs.pop('data_dict')
		super(EditProfileForm,self).__init__(*args,**kwargs)

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

		#check for no links
		if len(sc_list) == 0:
			print "No links entered."
			return False

		if self.data_dict['new'] == True:
			#remove any duplicates, method from http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
			seen = set()
			seen_add = seen.add
			unique_sc_list = [ x for x in sc_list if x not in seen and not seen_add(x)]
			print "hitting SC API"
			sc = SC_Embed(unique_sc_list)

			if sc[0] == False:
				raise forms.ValidationError(str(sc[1]) + " cannot be processed.")
			return sc[1]

		person_sc_links = self.data_dict['sc_list']
		person_sc_links = [i[0] for i in person_sc_links]

		person = self.data_dict['person']

		####TEMPORARY, later add a search bar for genres so users can input genres if none match requested genre
		####add in case where there are no sc/are all deleted
		#grab links to be deleted, identify new links, do nothing to old links
		trash_links = []
		new_sc_links = []
		unchanged_sc_links = []


		#case for no change between new and olds
		if sc_list == person_sc_links:
			print "no change"
			return False


		for l in sc_list: #current list
			print l
			if l in person_sc_links: #new list
				unchanged_sc_links.append(l) #think i don't actually need this
			else:
				new_sc_links.append(l) 

		#delete trash_links
		# print person_sc_links ,"PERSON SC"
		# print sc_links,"SC"
		for l in person_sc_links:
			if l not in sc_links:
				# print l
				# print person.soundcloud_set.filter(url=l[0])
				count = 0
				for i in person.soundcloud_set.filter(url=l):
					person.soundcloud_set.filter(url=l).delete()
					person.save() #do I need this?
					count += 1

		#check for no new links (already checked for no change), so this means 
		#links have been deleted
		if not new_sc_links:
			print "Links have been removed"
			return 
			
		print "hitting SC API"
		sc = SC_Embed(new_sc_links)

		if sc[0] == False:
			raise forms.ValidationError(str(sc[1]) + " cannot be processed.")

		# print unchanged_sc_links,"un"
		# print new_sc_links,"new"
		# print sc
		return sc[1]

	def clean_quote(self):
		quote = self.cleaned_data['quote']
		return quote