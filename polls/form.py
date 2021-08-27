
from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

	widgets = {
		 'username' : forms.TextInput(attrs={'class':'form-control'}),
		 'password' : forms.PasswordInput(attrs={'class':'form-control'})
		 }

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']


	widgets = {
		 'username' : forms.TextInput(attrs={'class':'form-control'}),
		 'password' : forms.PasswordInput(attrs={'class':'form-control'})
		 }
print("i csome changed from hotfix branch")