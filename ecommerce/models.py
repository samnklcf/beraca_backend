from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
import uuid



# Create your models here.

class categorie(models.Model):
    titre = models.CharField(max_length=50, null=False)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(verbose_name=("Image"), upload_to="product")
    
    date = models.DateField(auto_now=True)
    
    

    

    class Meta:
        verbose_name = ("Catégorie")
        verbose_name_plural = ("Catégories")

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs) 

    



class article(models.Model):
    
    nom = models.CharField(verbose_name=("Nom du produit"), max_length=100, null=False)
    slug = models.SlugField(null=True, blank=True)
    description = tinymce_models.HTMLField(verbose_name=("Description"), null=False)
    prix = models.PositiveIntegerField(verbose_name=("Prix"), null=False)
    rabais = models.PositiveIntegerField(verbose_name=("Prix après rabais"), null=True, default=0)
    date = models.DateField(auto_now=True)
    image1 = models.ImageField(verbose_name=("Image1"), upload_to="product")
    image2 = models.ImageField(verbose_name=("Image2"), upload_to="product")
    image3 = models.ImageField(verbose_name=("Image3"), upload_to="product")
    categorie = models.ForeignKey(categorie, verbose_name=("Catégorie"), on_delete=models.CASCADE)
    
    
    

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs) 
        
        

class news(models.Model):
    
    titre = models.CharField(verbose_name=("Nom du produit"), max_length=100, null=False)
    slug = models.SlugField(null=True, blank=True)
    mini_description = models.TextField(verbose_name=("Petite description"), null=False)
    description = models.TextField(verbose_name=("Description"), null=False)
    date = models.DateField(auto_now=True)
    image = models.ImageField(verbose_name=("Image"), upload_to="product")
    
    
    

    class Meta:
        verbose_name = ("New")
        verbose_name_plural = ("News")

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs) 

   
   
class Client(models.Model):
    choix = [
        ("Homme", "Homme"),
        ("Femme", "Femme"),
    ]
    nom = models.CharField(("Nom complet"), max_length=50, null=False)
    email = models.EmailField(verbose_name=("Votre email"), max_length=254)
    telephone = models.CharField(verbose_name=("Votre numéro de téléphone"), max_length=50)
    genre = models.CharField(max_length=80, choices=choix)
    date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")
    
    
class Commande(models.Model):
    choix_pays = [
        ("GABON","GABON"),
        
    ]
    
    choix_province = [
        
        ("LIBREVILLE","LIBREVILLE"),
        ("MOANDA","MOANDA"),
        ("LASTOURVILLE","LASTOURVILLE"),
        ("KOULAMOUTOU","KOULAMOUTOU"),
        ("FRANCEVILLE","FRANCEVILLE"),
        
    ]
    choix_statut= [
        
        ("livré","livré"),
        ("non-livré","non-livré"),
        
        
    ]
    
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    
    nom = models.CharField(max_length=50, null=False, verbose_name="nom et prénom")
    slug = models.SlugField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=False)
    telephone = models.CharField(verbose_name=("Numéro de téléphone"), max_length=50, null=False)
    adresse = models.CharField(verbose_name=("Votre adresse"), max_length=50, null=False)
    identifiant = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="quantité", default=1)
    pays = models.CharField(verbose_name="Pays", max_length=50, choices=choix_pays, default="GABON")
    province = models.CharField(verbose_name=("Ville"), max_length=50, choices=choix_province)
    boite = models.CharField(verbose_name=("Boîte Postal"), max_length=50, null=False)
    state = models.CharField(verbose_name=("Statut"), max_length=50, choices=choix_statut, default="non-livré")
    date = models.CharField(verbose_name=("Date de la commande"), max_length=50, null=False)
    


   

    class Meta:
        verbose_name = ("Commande")
        verbose_name_plural = ("Commandes")

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        self.identifiant = (uuid.uuid4())
        super().save(*args, **kwargs)



    
class section1(models.Model):

    titre = models.CharField(max_length=100, null=True)
    contenu = tinymce_models.HTMLField(verbose_name='Contenu', null=True, blank=True)
    image = models.ImageField("Image", upload_to="section1/image", null=False, blank=True)
    video = models.FileField(("Vidéo"), upload_to="section1/image", max_length=100, null=True, blank=True)
    bouton = models.CharField(("Texte du bouton"), max_length=50)
    date = models.DateField(verbose_name="Date", null=True, blank=True)
    

    class Meta:
        verbose_name = ("section1")
        verbose_name_plural = ("section1s")

    def __str__(self):
        return self.titre

   

# -----------------------contactez nous ---------------------------
class contact(models.Model):
    nom = models.CharField(("Nom"), max_length=500)
    email = models.EmailField(("Email"), max_length=254)
    telephne = models.IntegerField(("Telephne"))
    sujet = models.CharField(("Sujet"), max_length=5000)
    message = tinymce_models.HTMLField(("Message"), max_length=30000)
    
    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

  



# -------------------------------demande emploi --------------------------------

class demande(models.Model):
    choix_experience= [
        
        ("Oui","Oui"),
        ("Non","Non"),
        
        
    ]
    
    choix_validation= [
        
        ("Non-validé","Non-validé"),
        ("Validé","Validé"),
        
        
    ]
    
    nom = models.CharField(("Nom complet"), max_length=50, null=False)
    identifiant = models.CharField(max_length=50, null=True, blank=True, unique=True)
    email = models.EmailField(("Email"), max_length=254, null=True, blank=True)
    telephone = models.CharField(("Numéro de téléphone"), max_length=10, null=False, unique=True)
    adresse =  models.CharField(("Adresse"), max_length=200, null=False)
    ville = models.CharField(("Ville"), max_length=200, null=False)
    experience = models.CharField(("Expérience"), max_length=100, choices=choix_experience, null=False)
    raison = tinymce_models.HTMLField(verbose_name="Pourquoi?", max_length=5000, null=False)
    valide =models.CharField(("Validé ?"), max_length=50, null=False, blank=True,choices=choix_validation, default="Non-validé")
    slug = models.SlugField(null=True, blank=True)
    date = models.DateField(("Date"), auto_now=True)
    
    
    
    

    class Meta:
        verbose_name = ("demande")
        verbose_name_plural = ("demandes")

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        self.identifiant = (uuid.uuid4())
        super().save(*args, **kwargs)
    
    
class apropos(models.Model):
    titre = models.CharField(("Titre"),max_length=200, null=False, blank=True)
    image = models.ImageField(("Image"), upload_to="about")
    contenu = tinymce_models.HTMLField(verbose_name="Contenu", null=False, blank=True)
    date = models.DateField(("Date"), auto_now=True)
    
    

    class Meta:
        verbose_name = ("A propos")
        verbose_name_plural = ("A propos")

    def __str__(self):
        return self.titre

class collaborateur(models.Model):
    nom = models.CharField(("Nom complet"), max_length=50, null=False)
    image = models.ImageField(("Image"), upload_to="Collaborateur", blank=True, null=False)
    poste = models.CharField(("Poste"), max_length=50, null=False, blank=True)


    class Meta:
        verbose_name = ("Collaborateur")
        verbose_name_plural = ("Collaborateurs")

    def __str__(self):
        return self.nom


class telephone(models.Model):
    num = models.CharField(("Numero de téléphone"), max_length=200)
    

    class Meta:
        verbose_name = ("Mon téléphone")
        verbose_name_plural = ("Mon téléphone")

    def __str__(self):
        return self.num

   
class email(models.Model):
    email = models.EmailField(("Email"), max_length=254)
    

    class Meta:
        verbose_name = ("Mon email")
        verbose_name_plural = ("Mon email")

    def __str__(self):
        return self.email

   
class formation(models.Model):
    titre = models.CharField("Titre",max_length=200, null=False, blank=True)
    contenu = tinymce_models.HTMLField(verbose_name='Contenu', null=True, blank=True)
    image = models.ImageField("Image", upload_to="Formation/image", null=False, blank=True)
    date = models.DateField(verbose_name="Date", null=True, blank=True)
    
    

    class Meta:
        verbose_name = ("Formation")
        verbose_name_plural = ("Formations")

    def __str__(self):
        return self.titre

 
   

   
