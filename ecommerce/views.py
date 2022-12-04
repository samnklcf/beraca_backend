from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
import datetime

from .models import *
from .forms import *


# Create your views here.
def home(request):
    categories = categorie.objects.all()
    num = telephone.objects.all()[:1]
    formations = formation.objects.all()[:1]
    emails = email.objects.all()[:1]
    sections = section1.objects.all().order_by('-date')[:1]
    sections = section1.objects.all().order_by('-date')[:1]
    new = news.objects.all()
    articles = article.objects.all()[:10]
    
    return render(request, 'ecommerce/home.html', locals())



def detail(request, slug):
    categories = categorie.objects.all()
    
    num = telephone.objects.all()[:1]
    emails = email.objects.all()[:1]
    
    articles = article.objects.get(slug=slug)
    
    
    # commentaires = theme.commentaire_set.all()
    # cats = Category.objects.all()
    # p = Paginator(cats, 10)
    # page = request.GET.get('categorie')
    # cat = p.get_page(page)
        
    # if request.method == 'POST':
    #     user = request.user
    #     theme_id = request.POST['theme_id']
    #     identifiant = request.POST['identifiant']
    #     prix = request.POST['prix']
        
    #     ident = historique.objects.filter(user=user)
    #     for i in ident:
    #         if identifiant == i.identifiant:
    #             break
    #     else:
    #         story = historique(user=user, theme_id=theme_id, identifiant=identifiant, prix=prix)
    #         story.save()
                
        
        
    #     return redirect(f"../../lessonvideo/{identifiant}")
    
    
    
   
    # context = {
    #     "theme" : theme,
    #     "commentaires": commentaires,
    #     'cat': cat,
    #     "dts": dts,
    # }
    
    return render(request, 'ecommerce/detail.html', locals())
 
def parcat(request, slug):
    emails = email.objects.all()[:1]
    num = telephone.objects.all()[:1]
    categories = categorie.objects.all()
    cat = categorie.objects.get(slug=slug)
    articles = cat.article_set.all()
    return render(request, 'ecommerce/parcat.html', locals())


def commande(request, slug):
    categories = categorie.objects.all()
    emails = email.objects.all()[:1]
    num = telephone.objects.all()[:1]
    date = datetime.datetime.now().date()
    
    
    articles = article.objects.get(slug=slug)
    if request.method == "POST":
        non = False
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.article = articles
            form.instance.date = date
            form.save()
            return redirect('/')
    else:
        non = True
        form = CommandeForm()

    return render(request, 'ecommerce/commande.html', locals())

# -------------------------demandes------------------------

def exist(request):
    categories = categorie.objects.all()
    num = telephone.objects.all()[:1]
    emails = email.objects.all()[:1]
    return render(request, 'ecommerce/exist.html', locals())

def emploi(request): 
    categories = categorie.objects.all()
    num = telephone.objects.all()[:1]
    emails = email.objects.all()[:1]
   
    if request.method == "POST":
        non = False
        tel = False
            
        form = DemandeForm(request.POST)
        if form.is_valid():
                
            form.save()
            return redirect('merci')
        return redirect('exist')       
    else:
            
        non = True
        form = DemandeForm()  
            
            
        
    return render(request, 'ecommerce/emploi.html', locals())

# ------------------merci--------------------------

def merci(request):
    categories = categorie.objects.all()
    emails = email.objects.all()[:1]
    
    num = telephone.objects.all()[:1]
    return render(request, 'ecommerce/merci.html', locals())

# ------------------------about-------------------

def about(request):
    categories = categorie.objects.all()
    abouts = apropos.objects.all()[:1]
    collab = collaborateur.objects.all()
    num = telephone.objects.all()[:1]
    emails = email.objects.all()[:1]
    return render(request, 'ecommerce/about.html', locals())


def contact(request):
    collab = collaborateur.objects.all()
    num = telephone.objects.all()[:1]
    categories = categorie.objects.all()
    if request.method == "POST":
        non = False
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('merci')
        return redirect('exist')
    else:
        non = True
        form = ContactForm()
    return render(request, 'ecommerce/contact.html', locals())