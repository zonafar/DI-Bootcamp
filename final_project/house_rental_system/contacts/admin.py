from django.contrib import admin
from contacts.models import Contact 

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'annonce','email','phone', 'date_contact')
    list_display_links = ('id','nom')
    search_fields = ('nom', 'annonce','email','phone')
    list_per_page = 30

