from django.db import models

# Create your models here.

class Element(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=3)
    atomic_mass = models.CharField(max_length=200)
    am_unit = models.CharField(max_length=10)


    def __str__(self):
        return self.name




class Molecule(models.Model):
    name = models.CharField(max_length=200)
    formula = models.CharField(max_length=50)
    molecular_weight = models.FloatField(max_length=10)
    mw_unit = models.CharField(max_length=10)
    inchikey= models.CharField(max_length=50, default=None, null=True)
    elements = models.ManyToManyField(Element, blank=True)

    def __str__(self):
        return self.name



