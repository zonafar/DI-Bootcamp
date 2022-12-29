from django.shortcuts import render, redirect
from films.models import *
from films.forms import *

# Create your views here.

def home(request):
    films = Film.objects.all()
    context = {
        'page_title' : "SignUp",
        'films' : films
    }
    return render(request, 'homepage.html', context)


def add_director(request):
    context = {
        'page_title' : "SignUp",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = AddDirectorForm(request.POST) # the Person Form
        # check if it's valid:
        if form.is_valid():
            new_director = form.save()
            print(new_director)
            return redirect('home')
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'director/addDirector.html', context)

    else:
        # GET, generate blank form
        context['form'] = AddDirectorForm()
    return render(request, 'director/addDirector.html', context)


def add_film(request):
    context = {
        'page_title' : "SignUp",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = AddFilmForm(request.POST) # the Person Form
        # check if it's valid:
        if form.is_valid():
            new_film = form.save()
            print(new_film)
            return redirect('home')
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'film/addFilm.html', context)

    else:
        # GET, generate blank form
        context['form'] = AddFilmForm()
    return render(request, 'film/addFilm.html', context)