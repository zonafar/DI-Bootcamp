from django.shortcuts import render

# Create your views here.
people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def all_people(request):
    context = {}
    context['people'] = people
    return render(request, "list_of_people.html", context)

def unique_people(request,id):
    context = {}
    for p in people:
        if p['id'] == id:
            context['person'] =  p
            break
    return render(request, "one_people.html",context)