from django.db import models
from django.contrib.auth.models import User
from prodotti.models import Product  

# Create your models here.
class Indirizzo(models.Model):
    via = models.CharField(max_length=50)
    civico = models.CharField(max_length=50)
    cap = models.CharField(max_length=50)
    citta = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    stato = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    
    
class OrdineEffettuato(models.Model):
    id_utente = models.ForeignKey(User, on_delete=models.CASCADE)
    id_indirizzo = models.ForeignKey(Indirizzo, on_delete=models.CASCADE)
    id_prodotto = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    

