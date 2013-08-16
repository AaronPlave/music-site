import datetime
from haystack import indexes
from Profile.models import *

class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
	
	text = indexes.CharField(document=True, use_template=True)
	location = indexes.CharField(model_attr='location')
	genre = indexes.CharField(model_attr='genre')
	instruments = indexes.CharField(model_attr='instruments')

	#autocomplete
	content_auto = indexes.EdgeNgramField(model_attr='User')


	def get_model(self):
		return Profile

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.all()
