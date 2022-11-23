from django.shortcuts import render,redirect
from todo.forms import AddTodoForm
from todo.models import *

# Create your views here.


def todo(request):
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.create(
                title = form.cleaned_data['title'],
                details = form.cleaned_data['details'],
                deadline_date = form.cleaned_data['deadline_date'],
                category = Category.objects.get(id = form.cleaned_data['category'])
            )
            todo.save()
            return redirect('display_todos')
        return render(request,'todo.html',{'form':form})
    else:
        form = AddTodoForm()
    return render(request,'todo.html',{'form':form})



def display_todos(request):
    todos = Todo.objects.all()
    return render(request,'display_todos.html',{'todos':todos})
