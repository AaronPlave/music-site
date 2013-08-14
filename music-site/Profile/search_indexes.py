import datetime
from haystack import indexes
from Profile.models import *

class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
	print "CLASSING"
	
	text = indexes.CharField(document=True, use_template=True)
	location = indexes.CharField(model_attr='location')
	genre = indexes.CharField(model_attr='genre')
	instruments = indexes.CharField(model_attr='instruments')

	#autocomplete
	content_auto = indexes.EdgeNgramField(model_attr='User')


	def get_model(self):
		print "MODEL"
		return Profile

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		print "INDEX HERE!"
		return self.get_model().objects.all()
