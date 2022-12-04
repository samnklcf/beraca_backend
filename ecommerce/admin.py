from django.contrib import admin
from .models import *

admin.site.site_header = "BERACA"

class AdminArticle(admin.ModelAdmin):
    list_display = (id,"nom", "prix", "categorie", ) 
    
class AdminCommande(admin.ModelAdmin):
    list_display = ("nom", "email", "telephone","adresse","article","quantity","province","date" ,"state", ) 
    
class AdminDemande(admin.ModelAdmin):
    list_display = ("nom", "telephone","adresse","valide", "date") 
    



admin.site.register(categorie)
admin.site.register(Client)
admin.site.register(news)
admin.site.register(Commande, AdminCommande)
admin.site.register(article, AdminArticle)
admin.site.register(section1)
admin.site.register(demande, AdminDemande)
admin.site.register(apropos)
admin.site.register(collaborateur)
admin.site.register(telephone)
admin.site.register(email)
admin.site.register(formation)
admin.site.register(contact)


