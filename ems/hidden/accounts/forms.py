from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# inhirate UserCreationForm
class UserAddForm(UserCreationForm):
	'''
	Extending UserCreationForm - with email

	'''
	# add any filds you want (email and first name ) 
	# widget=forms.EmailInput(attrs={'placeholder':'eg.rajparmar@.com'}) # use to give deisne to or page , we send form| crispy 
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg.rajparmar@.com'}))
	first_name =forms.CharField(max_length=50)
	class Meta:
		model = User 
		fields = ['username', 'first_name' , 'email','password1','password2'] # the things to show in that form 
"""
	def __init__(self, *args: Any, **kwargs): # arg to pass any value (username , password)
		super(UserAddForm).__init__(*args, **kwargs) # form his super class 

		self.fields['username'].widget.attrs['class'] = 'form-control'  # desine the username filed by give a class form bootstart 
		self.fields['first_name'].widget.attrs['class'] = 'form-control'  # desine the username filed by give a class form bootstart 
		self.fields['email'].widget.attrs['class'] = 'form-control' # desine the username filed by give a class form bootstart 
		self.fields['password1'].widget.attrs['class'] = 'form-control' # desine the username filed by give a class form bootstart 
		self.fields['password2'].widget.attrs['class'] = 'form-control' # desine the username filed by give a class form bootstart 
"""
		

	





class UserLogin(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))


