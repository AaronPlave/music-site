from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=300)
	email = forms.EmailField(required=False)
	message = forms.CharField(widget=forms.Textarea)
