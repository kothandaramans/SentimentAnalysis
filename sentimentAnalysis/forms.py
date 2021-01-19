from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title		= forms.CharField(label='hello title',widget=forms.TextInput(
										attrs={
											'placeholder':'enter title'
										}))
	description	= forms.CharField(required=False, widget=forms.Textarea(
									attrs={
									 'class':'desc'
									}))
	price		= forms.DecimalField(initial=56)

	class Meta:
			model = Product
			fields = ['title','description','price','is_active']

	def clean_title(self):
		tle = self.cleaned_data.get('title')
		if 'sk' in tle:
			return tle
		else:
			raise forms.ValidationError('This is not a valid title')



class RProduct(forms.Form):
	title		= forms.CharField(label='hello title',widget=forms.TextInput(
										attrs={
											'placeholder':'enter title'
										}))
	description	= forms.CharField(required=False, widget=forms.Textarea(
									attrs={
									 'class':'desc'
									}))
	price		= forms.DecimalField(initial=56)