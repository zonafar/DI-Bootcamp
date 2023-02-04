from django.contrib import admin
from location.models import * 

# Register your models here.

@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'is_published','prix', 'date_annonce','agent')
    list_display_links = ('id','titre')
    list_filter = ('agent',)
    list_editable = ('is_published',)
    search_fields = ('titre', 'description', 'adresse','ville', 'secteur', 'region', 'prix')
    list_per_page = 20

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom','email', 'date_embauche')
    list_display_links = ('id','nom')
    search_fields = ('nom','prenom')
    list_per_page = 20

# Need to be at the end
# admin.site.register(Annonce)
# admin.site.register(Agent)
