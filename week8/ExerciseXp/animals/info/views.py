from django.shortcuts import render
import json

# Create your views here.
file = "C:/Users/ZONA/3D Objects/Orange DI/DI-Bootcamp/week8/ExerciseXp/animals/animals.json"
with open(file) as f: 
    data = json.load(f)

def animal(request,animal_id,):
    context = {}
    for animal in data['animals']:
        if animal['id'] == animal_id:
            context['animal'] = animal
            break
    # raise Exception(f"I want to know the value of this: {context}")
    return render(request, "animal.html", context)

def family(request,family_id):
    context = {}
    for family in data['families']:
        if family['id'] == family_id:
            context['family'] = family
            break
    # raise Exception(f"I want to know the value of this: {context}")
    print(context)
    return render(request, "family.html", context)