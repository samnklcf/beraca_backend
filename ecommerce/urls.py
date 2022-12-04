from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('detail/<str:slug>', detail, name="detail"),
    path('commande/<str:slug>', commande, name="commande"),
    path('merci', merci, name="merci"),
    path('exist', exist, name="exist"),
    path('demande/emploi', emploi, name="demande"),
    path('apropos', about, name="apropos"),
    path('contact', contact, name="contact"),
    path('catégorie/<str:slug>', parcat, name="parcat"),
]
