from django.urls import path,include
from . import views

urlpatterns = [
    path('add/', views.todo, name ='add_todo'),
    path('display/', views.display_todos,name ='display_todos'),
]