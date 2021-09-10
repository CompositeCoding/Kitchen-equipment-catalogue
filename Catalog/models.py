from django.db import models

# Create your models here.
class Products(models.Model):
    Typenummer = models.CharField(max_length=40, primary_key=True )
    Lijn = models.CharField(max_length=20)
    Code = models.CharField(max_length=20, null=True)
    Categorie = models.CharField(max_length=60)
    kW = models.CharField(max_length=20, null=True)
    Voltage = models.CharField(max_length=20, null=True)
    Afmetingen = models.CharField(max_length=30, null=True)
    Breedte = models.CharField(max_length=30, null=True)
    Diepte = models.CharField(max_length=30, null=True)
    Hoogte = models.CharField(max_length=30, null=True)
    Aansluiting = models.CharField(max_length=30, null=True)
    Inhoud = models.CharField(max_length=30, null=True)
    Prijs = models.IntegerField()
    Extra = models.CharField(max_length=500, null=True)
    Bedrijf = models.CharField(max_length=30, null=False)
