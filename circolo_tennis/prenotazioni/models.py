from django.db import models
from django.contrib.auth.models import User

class PrenotazioneCampo(models.Model):
    campo_choices = [
        ('Campo 1', 'Campo 1'),
        ('Campo 2', 'Campo 2'),
        ('Campo 3', 'Campo 3'),
    ]

    campo = models.CharField(max_length=10, choices=campo_choices)
    orario = models.TimeField()
    data = models.DateField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    settimana = models.IntegerField()
    durata = models.IntegerField(default=1)  # Durata in ore
    prenotato = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.campo} - {self.data} - {self.orario} - {self.cliente.username}"
