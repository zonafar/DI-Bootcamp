from django.shortcuts import render
from .models import Family,Animal# import the models from polls/models.py

# Create your views here.


def family(request,id):

    family = Family.objects.filter(id= id).first()
    animals = family.animal_set.all() 
    context = {
    'page_title' : family.name,
    'animals' : animals,
    }
    return render(request, 'family.html', context)

def animal(request,id):
    animal = Animal.objects.filter(id= id).first()
    context = {
    'page_title' : animal.name,
    'animal' : animal,
    }
    return render(request, 'animal.html', context)


def animals(request):
    animals =  Animal.objects.all() 
    context = {
    'page_title' : 'Animals',
    'animals' : animals,
    }
    return render(request, 'animals.html', context)