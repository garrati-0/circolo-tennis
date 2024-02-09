from django.db import models
from django.contrib.auth.models import User

class Recensione(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    testo = models.TextField()
    voto = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    data_creazione = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    prodotto = models.CharField(max_length=255)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    imagine = models.ImageField(upload_to='prodotti\static\img', blank=True, null=True)
    nomeimg = models.CharField(max_length=255)
    quantita = models.PositiveIntegerField(default=0)
    recensioni = models.ManyToManyField(Recensione, related_name='recensioni_prodotto', blank=True)

class Preferiti(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Product, on_delete=models.CASCADE)
