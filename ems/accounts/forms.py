from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


# costumaze user createion to add emal to regerstring procses 
class CreationUserForm(UserCreationForm):
	class Meta :
		model = User
		fields = ['username','email','password1','password2']


class CreationUserForm(UserCreationForm):
	class Meta :
		model = User
		fields = ['email','first_name','last_name']


class UserAddForm(UserCreationForm):
	'''
	Extending UserCreationForm - with email

	'''
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg.rajparmar@.com'}))

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		

	





class UserLogin(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))


class User_Update_Profile(ModelForm):
	class Meta :
		model = User
		fields = ['first_name','last_name','email']


class User_Update_Profile_test(ModelForm):
	class Meta :
		model = Profile
		fields = ['name','phone','profile_image']
"""	class Meta :
		model = profile
		fields = '__all__'
		exclude = ['user']"""
"""        
class Update_Profile(forms.ModelForm):
	
	class Meta:
		model = profile
		exclude = ['user']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}
"""
class SignUpForm(UserCreationForm):
	"""
	email = forms.EmailField(label="",widget= forms.TextInput(attrs={'class':'form-control','placeholder':"Email Address"}))
	first_name = forms.CharField(label="",max_length=100,widget= forms.TextInput(attrs={'class':'form-control','placeholder':"First Name"}))
	last_name = forms.CharField(label="",max_length=100,widget= forms.TextInput(attrs={'class':'form-control','placeholder':"Last Name"}))
	"""
	class Meta:
		model = User
		fields = ['username','password1','password2']

class ProfilePicForm(forms.ModelForm):
	profile_image = forms.ImageField(label="Profile Picter" )
	# save the image in proifle form accpimts models.py (note that model extends user model and has column called profile_image)
	class Meta:
		model = Profile
		fields = ('profile_image', )
