from django.urls import path
from contacts import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('<int:id>/contact/', views.detail_contact, name='detail_contact'),
]