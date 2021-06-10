from django import forms
from crudapp.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"
		widgets={
			
			"name":forms.TextInput(attrs={'class':'form-control'}),
			"email":forms.EmailInput(attrs={'class':'form-control'}),
			"password":forms.TextInput(attrs={'class':'form-control'})
			
		}