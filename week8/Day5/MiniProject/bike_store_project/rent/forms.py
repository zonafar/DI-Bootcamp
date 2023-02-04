from django import forms
from rent.models import *


vehicles = Vehicle.objects.filter(rented=False)
customers = Customer.objects.all()

v_choices = [(v.id,v.vehicle_type) for v in vehicles]
c_choices = [(c.id,c.first_name+" "+c.last_name) for c in customers]

class rentalForm(forms.Form):
    rental_date = forms.DateTimeField(widget = forms.SelectDateWidget)
    # return_date = forms.DateField(widget = forms.SelectDateWidget)
    vehicle = forms.ChoiceField(choices = v_choices,widget=forms.Select)
    customer = forms.ChoiceField(choices = c_choices,widget=forms.Select)


