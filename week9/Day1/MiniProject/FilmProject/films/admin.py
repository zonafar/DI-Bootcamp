from django.contrib import admin
from films.models import *

# Register your models here.

admin.site.register(Film)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Director)