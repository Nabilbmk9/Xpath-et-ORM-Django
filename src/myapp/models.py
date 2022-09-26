from django.db import models

# Create your models here.
#Écrire une classe Personne ayant comme attributs : un nom, prénom, date de naissance.
class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()