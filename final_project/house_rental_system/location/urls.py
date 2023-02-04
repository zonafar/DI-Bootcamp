from django.urls import path
from . import views
from location.models import * 
from location.forms import * 

# urlpatterns = [
#     path('propriete/', views.propriete_get_all,name = "location.propriete_get_all"),

#     path('propriete/<int:pk>/', views.propriete_get,name = "location.propriete_get"),
#     path('propriete/add/', views.propriete_add,name = "location.propriete_add"),
#     path('propriete/edit/<int:pk>/', views.propriete_edit,name = "location.propriete_edit"),
#     path('propriete/delete/<int:pk>/', views.propriete_delete,name = "location.propriete_delete")

# ]

urlpatterns = [

    path('', views.index,name='index'),
    path('about/', views.about,name='about'),

    # path('home/', views.HomeView.as_view(), name='home'),

    # Link for Propriete
    # path('add-propriete/', views.CreateView.as_view(), name='AddPropriete'),
    # path('update-propriete/<int:id>/', views.ProprieteUpdateView.as_view(), name='UpdatePropriete'),
    # path('<pk>/delete/', views.DeleteView.as_view()),

    # Link for Description 
    # path('add-description/', views.CreateView.as_view(model = Description, template_name = 'description/addDescription.html',form_class = DescriptionForm), name='AddDescription'),


    # path('update-service/<int:id>/', views.ProprieteUpdateView.as_view(), name='UpdatePropriete'),
    # path('<pk>/delete/service', views.DeleteView.as_view()),
]

