from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ("__all__")
        exclude = ('slug','idantifiant','state', "article","date",)
        

class DemandeForm(forms.ModelForm):
    class Meta:
        model = demande
        fields = ("__all__")
        exclude = ('validate','slug', 'identifiant')
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ("__all__")
       