from django.db import models
from django.contrib.auth.models import User
from prodotti.models import Product  
from impostazioni.models import Indirizzo
    
class OrdineEffettuato(models.Model):
    id_utente = models.ForeignKey(User, on_delete=models.CASCADE)
    id_indirizzo = models.ForeignKey(Indirizzo, on_delete=models.CASCADE)
    id_prodotto = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    

