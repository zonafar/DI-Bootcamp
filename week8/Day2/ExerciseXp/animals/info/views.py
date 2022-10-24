from django.shortcuts import render
from .models import Family,Animal# import the models from polls/models.py

# Create your views here.


def family(request,id):

    family = Family.objects.filter(id= id).first()
    # animals = family.animal_set.all() 
    animals = family.animal_set.all().order_by('name').values()
    counter = family.animal_set.count()
    context = {
    'page_title' : family.name,
    'animals' : animals,
    'counter' : counter
    }
    return render(request, 'family.html', context)

def animal(request,id):
    animal = Animal.objects.filter(id= id).first()
    # family = Animal.objects.filter(family__pk=animal.id)
    family = animal.family
    # raise Exception(f'famille : {family.id}')
    context = {
    'page_title' : animal.name,
    'animal' : animal,
    'family' : family.id
    }
    return render(request, 'animal.html', context)


def animals(request):
    animals_by_family =  Animal.objects.all().order_by('family__name','name').values()
    animals_by_speed =  Animal.objects.all().order_by('speed').values()
    context = {
    'page_title' : 'Animals',
    'animals' : animals_by_speed,
    }
    return render(request, 'animals.html', context)