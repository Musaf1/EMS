from .models import Employees , LinkUser , pirod
from django import forms

class employeesForm(forms.Form):
    
    class meta:
        model = Employees
        fields = '__all__'

class EmployeeCreateForm(forms.ModelForm):
	employeeid = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'please enter 5 characters without RGL or slashes eg. A0025'}))
	image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'previewImage(this);'}))
	class Meta:
		model = Employees
		exclude = ['is_blocked','is_deleted','created','updated']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}
        
class LinkUserForm(forms.ModelForm):
	
	class Meta:
		model = LinkUser
		exclude = ['is_blocked','is_deleted','employeetype' , 'dateissued']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}

class attendaceForm(forms.ModelForm):

	class Meta:
		model = pirod
		fields = '__all__'
		'''start_perod = forms.DateInput()
		end_perod= forms.DateInput()'''
# take format csf pdf ...
format_chosis = (
	('xls','xls'),
	('csv','csv'),
	('json','json'),
)
class formFormat(forms.Form):
	format = forms.ChoiceField(choices=format_chosis,widget=forms.Select(attrs={'class':'form-select'})) # widget to use nice form for bootstarb
    