from django.urls import path
from . import views 

urlpatterns = [
    path('<int:id>/annonce/', views.annonce , name = 'annonce'),
    path('', views.annonces , name = 'annonces'),
    path('search/', views.search , name = 'search'),
]
