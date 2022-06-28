from unicodedata import name
from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    img = models.ImageField(upload_to="galeria")
    def __str__(self):
        return self.name

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    name = models.CharField(max_length=50)
    correo = models.EmailField()
    fono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return self.rut + " " + self.name