from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class registerForm(UserCreationForm):
	last_name = forms.CharField(label = "Prenom",required=True)
	first_name = forms.CharField(label = "Nom", required=True)
	email = forms.EmailField(required=True)
	username = forms.CharField(required=True, label  = "Nom d'utlisateur")

	class Meta:
		model = User
		fields = ("first_name","last_name","username","email", "password1", "password2")

	def save(self, commit=True):
		user = super(registerForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.last_name = self.cleaned_data['last_name']
		user.first_name = self.cleaned_data['first_name']
		user.username = self.cleaned_data['username']
		if commit:
			user.save()
		return user


