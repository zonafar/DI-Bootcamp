from django.urls import path
from . import views

urlpatterns = [
    path('rental/', views.rentals,name = "rent.rentals"),
    path('rental/<int:pk>', views.rental,name = "rent.rental"),
    path('rental/add/', views.rental_add,name = "rent.rental_add"),

    path('customer/<int:pk>', views.customer,name = "rent.customer"),
    path('customer/', views.customers,name = "rent.customers"),
    path('customer/add/', views.customer_add,name = "rent.customer_add"),

    path('vehicle/<int:pk>', views.vehicle,name = "rent.vehicle"),
    path('vehicle/', views.vehicles,name = "rent.vehicles"),
    path('vehicle/add/', views.vehicle_add,name = "rent.vehicle_add"),
    path('rental/return/<int:pk>', views.vehicle_return,name = "rent.vehicle_return"),
    
]