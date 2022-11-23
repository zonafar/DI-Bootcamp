from .models import Todo,Category
from django import forms

categories = [(cat.id,cat.name) for cat in Category.objects.all()]
# print(categories)
# categories = Category.objects.all()


class AddTodoForm(forms.Form):
    title = forms.CharField()
    category = forms.ChoiceField(choices = categories)
    details = forms.CharField(widget = forms.Textarea)
    deadline_date = forms.DateTimeField(widget = forms.SelectDateWidget)
    # class Meta:
    #     model = Todo
    #     fields = ['title','details','deadline_date','category']


