from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=300)
	email = forms.EmailField(required=False, label='Your e-mail addres')
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		"""
		Django form system knows to look for method whose name
		starts with clean__ and ends with the name of a field. 
		If any such method exists, it's called during validation.
		"""
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message