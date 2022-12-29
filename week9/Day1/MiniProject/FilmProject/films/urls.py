from django.urls import path 
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('home/', views.home, name='home'),
    path('add-film/', views.add_film, name='AddFilm'),
    path('add-director/', views.add_director, name='AddDirector'),
]