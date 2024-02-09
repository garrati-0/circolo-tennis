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



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_profilo = models.ImageField(upload_to='home\static\img', blank=True, null=True)
    nomefoto = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username