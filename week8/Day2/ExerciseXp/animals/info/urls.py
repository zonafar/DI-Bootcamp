from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('family/<int:id>/', views.family, name='family'),
    path('animal/<int:id>/', views.animal, name='animal'),
    path('animals/', views.animals, name='animals'),
]
