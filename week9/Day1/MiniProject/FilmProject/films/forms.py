from django import forms
from films.models import *

class AddFilmForm(forms.ModelForm):
    class Meta:      
        model = Film
        exclude = ['released_date']
        # we can add some widget : here helper class to display the form in the template
        # widgets = {
        #     'text': forms.Textarea(attrs={'class': 'textarea'}),
        #     'author': forms.Select(attrs={'class': 'select'})
        # }


class AddDirectorForm(forms.ModelForm):
    class Meta:      
        model = Director
        fields = '__all__'