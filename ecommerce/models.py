from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=35)

    def __str__(self):
        return self.nome

class Product(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length = 35)
    prezzo = models.FloatField()
    disponibilità = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class User(models.Model):
    nome = models.CharField(max_length = 35)
    cognome = models.CharField(max_length = 35)
    email = models.CharField(max_length = 35)
    password = models.CharField(max_length = 8)

    def __str__(self):
        return self.email

class Order(models.Model):
    numero = models.IntegerField()
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    prodotti = models.ManyToManyField(Product)
    totale = models.FloatField()

    def __str__(self):
        return str(self.numero)