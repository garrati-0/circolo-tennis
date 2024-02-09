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
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    settimana = models.IntegerField()
    durata = models.IntegerField(default=1)  # Durata in ore
    prenotato = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.campo} - {self.data} - {self.orario} - {self.cliente.username}"
    

class Lobby(models.Model):
    CREATOR_CHOICES = [
        ('Singolo', 'Singolo'),
        ('Doppio', 'Doppio'),
    ]

    LEVEL_CHOICES = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Esperto', 'Esperto'),
    ]

    creator = models.ForeignKey(User, related_name='created_lobbies', on_delete=models.CASCADE)
    tipo_partita = models.CharField(max_length=10, choices=CREATOR_CHOICES)
    livello = models.CharField(max_length=20, choices=LEVEL_CHOICES)  # Livello del giocatore
    numero_giocatori = models.IntegerField(default=1)  # Numero di giocatori attualmente nella lobby
    prenotazione_campo = models.ForeignKey(PrenotazioneCampo, related_name='related_lobby', on_delete=models.CASCADE, null=True, blank=True)
    pubblicata = models.BooleanField(default=False)  # Flag per indicare se la lobby è pubblicata o meno

    def __str__(self):
        return f"Lobby {self.id} - Creatore: {self.creator.username} - Tipo partita: {self.tipo_partita} - Livello: {self.livello}"

    @property
    def max_giocatori(self):
        if self.tipo_partita == 'Singolo':
            return 2  # Numero massimo di giocatori per il singolo
        elif self.tipo_partita == 'Doppio':
            return 4  # Numero massimo di giocatori per il doppio

    def aggiungi_giocatore(self, user):
        if self.numero_giocatori < self.max_giocatori:
            self.numero_giocatori += 1
            self.save()

    def rimuovi_giocatore(self, user):
        if self.numero_giocatori > 0:
            self.numero_giocatori -= 1
            self.save()

