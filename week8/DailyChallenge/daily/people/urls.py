from django.urls import path 
from . import views

urlpatterns = [
    path('people/',views.all_people,name = 'people'),
    path('people/<int:id>/',views.unique_people,name = 'unique_people'),
]
