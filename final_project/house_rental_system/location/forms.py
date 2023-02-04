# from django.forms import ModelForm
# from django import forms
# from location.models import *

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column

# vehicles = Vehicle.objects.filter(rented=False)
# customers = Customer.objects.all()

# v_choices = [(v.id,v.vehicle_type) for v in vehicles]
# c_choices = [(c.id,c.first_name+" "+c.last_name) for c in customers]

# class ProprieteForm(ModelForm):
#     class Meta:
#         model = Propriete
#         exclude = ['date_creation']
        
# class ProprieteDeleteForm(ModelForm):
#     class Meta:
#         model = Propriete
#         fields = []

# class VisiteurForm(forms.ModelForm):
#     class Meta:      
#         model = Visiteur
#         fields = '__all__'

# class ProprietaireForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('taille', css_class='form-group col-md-6 mb-0'),
#                 Column('chambres', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             'decrire',
#             Row(
#                 Column('image_1', css_class='form-group col-md-4 mb-0'),
#                 Column('image_2', css_class='form-group col-md-4 mb-0'),
#                 Column('image_3', css_class='form-group col-md-4 mb-0'),
#                 css_class='form-row'
#             ),
#             'publier',
#             Submit('submit', 'Soumettre')
#         )
#     class Meta:      
#         model = Proprietaire
#         fields = '__all__'

# class TypeForm(forms.ModelForm):
#     class Meta:      
#         model = Type
#         fields = '__all__'

# class CategorieForm(forms.ModelForm):
#     class Meta:      
#         model = Categorie
#         fields = '__all__'

# class VilleForm(forms.ModelForm):
#     class Meta:      
#         model = Ville
#         fields = '__all__'

# class SecteurForm(forms.ModelForm):
#     class Meta:      
#         model = Secteur
#         fields = '__all__'

# class DescriptionForm(forms.ModelForm):
#     class Meta:      
#         model = Description
#         fields = '__all__'



