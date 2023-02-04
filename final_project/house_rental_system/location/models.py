from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# # Create your models here.




# class Ville(models.Model):
#     nom = models.CharField(max_length=100)
#     def __str__(self):
#         return f"{self.nom}"

# class Secteur(models.Model):
#     nom = models.CharField(max_length=60)
#     numero = models.IntegerField()
#     ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.nom}-{self.numero} {self.ville.nom}"

# class Type(models.Model):
#     nom = models.CharField(max_length=60)
#     def __str__(self):
#         return f"{self.nom}"

# class Categorie(models.Model):
#     nom = models.CharField(max_length=60)
#     type = models.ForeignKey(Type, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.nom}"

class Agent(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=60)
    telephone = PhoneNumberField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField()
    email = models.CharField(max_length= 50,blank=True)
    # phone = models.CharField(max_length= 30,blank=True)
    is_MVP= models.BooleanField(default = False)
    date_embauche = models.DateField(default=timezone.now())
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Annonce(models.Model):
    titre = models.CharField(max_length=200,blank=True)
    adresse = models.CharField(max_length=125,blank=True)
    description = models.TextField(verbose_name='description')
    ville = models.CharField(max_length=100,blank=True)
    secteur = models.CharField(max_length=100,blank=True)
    region =  models.CharField(max_length=100,blank=True)
    code_postal = models.CharField(max_length=20,blank=True)
    prix = models.IntegerField()
    chambres = models.SmallIntegerField(default = 0)
    douches = models.SmallIntegerField(default = 0)
    garages = models.SmallIntegerField(default = 0)
    taille = models.DecimalField(max_digits=6, decimal_places=1)
    date_annonce = models.DateField(default=timezone.now())
    is_published = models.BooleanField(default = True)
    photo_majeure = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    # categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.titre} - {self.ville}"



# CHOIX_LOCATAIRE = [
#     ('F','Famille'),
#     ('I','Individu'),
#     ('E','Etudiant'),
#     ('A','Aucune précision'),
# ]
# class Description(models.Model):
#     locataire_prefere = models.CharField(max_length=3, choices=CHOIX_LOCATAIRE)
#     garage = models.BooleanField(default = False)
#     nombre_etage = models.SmallIntegerField()
#     niveau_etage = models.SmallIntegerField()
#     date_disponible = models.DateField()
#     balcon  = models.BooleanField(default = False)
#     meubles = models.BooleanField(default = False)
#     propriete = models.OneToOneField(
#         Propriete,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     def get_absolute_url(self):
#         return reverse('home')



# class Visiteur(models.Model):
#     nom = models.CharField(max_length=60)
#     password = models.CharField(max_length=100)
#     email = models.EmailField()
#     telephone = PhoneNumberField(blank=True)
#     propriete = models.ManyToManyField(Propriete,related_name='proprietes', blank=True)



