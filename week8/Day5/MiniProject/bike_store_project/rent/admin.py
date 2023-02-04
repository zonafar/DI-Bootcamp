from django.contrib import admin
from rent.models import * 

# Register your models here.

admin.site.register(Vehicle_Type)
admin.site.register(Vehicle_Size)
admin.site.register(Vehicle)
admin.site.register(Rental_Rate)
admin.site.register(Rental)