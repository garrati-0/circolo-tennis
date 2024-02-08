from django.db import models
from django.contrib.auth.models import User

class Indirizzo(models.Model):
    via = models.CharField(max_length=50)
    civico = models.CharField(max_length=50)
    cap = models.CharField(max_length=50)
    citta = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    stato = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='indirizzi')
