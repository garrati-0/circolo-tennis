# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import PrenotazioneCampo, Lobby
from django.urls import reverse

class MyFunctionTestCase(TestCase):
    def setUp(self):
        # Creazione di un utente per il test
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Creazione di una prenotazione per il test
        self.prenotazione = PrenotazioneCampo.objects.create(campo='Campo 1', orario='10:00:00', data='2024-01-01', cliente=self.user, settimana=1, durata=1, prenotato=False)

    def test_crea_lobby(self):
        # Simulazione di una richiesta POST
        data = {'tipo_partita': 'Singolo', 'livello': 'Doppio'}
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('crea_lobby', args=[self.prenotazione.id]), data)

        # Assicurati che la prenotazione sia stata correttamente recuperata
        prenotazione = PrenotazioneCampo.objects.get(id=self.prenotazione.id)
        self.assertIsNotNone(prenotazione)

        # Altri test a seconda di cosa vuoi verificare nella tua funzione

    def tearDown(self):
        # Pulizia dopo il test
        self.user.delete()
        self.prenotazione.delete()
        
        


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password123')

        self.prenotazione = PrenotazioneCampo.objects.create(
            campo='Campo 1',
            orario='12:00',
            data='2024-02-13',
            cliente=self.user,
            settimana=1,
            durata=1,
            prenotato=False
        )

        self.lobby = Lobby.objects.create(
            creator=self.user,
            tipo_partita='Singolo',
            livello='Principiante',
            numero_giocatori=1,
            prenotazione_campo=self.prenotazione,
            pubblicata=False
        )

    def test_prenotazionecampo_creation(self):
        print("Test creazione PrenotazioneCampo")
        self.assertEqual(self.prenotazione.campo, 'Campo 1')
        self.assertEqual(self.prenotazione.orario, '12:00')
        self.assertEqual(self.prenotazione.data, '2024-02-13')
        self.assertEqual(self.prenotazione.cliente, self.user)
        self.assertEqual(self.prenotazione.settimana, 1)
        self.assertEqual(self.prenotazione.durata, 1)
        self.assertFalse(self.prenotazione.prenotato)

    def test_lobby_creation(self):
        print("Test creazione Lobby")
        self.assertEqual(self.lobby.creator, self.user)
        self.assertEqual(self.lobby.tipo_partita, 'Singolo')
        self.assertEqual(self.lobby.livello, 'Principiante')
        self.assertEqual(self.lobby.numero_giocatori, 1)
        self.assertEqual(self.lobby.prenotazione_campo, self.prenotazione)
        self.assertFalse(self.lobby.pubblicata)

    def test_max_giocatori(self):
        print("Test numero massimo di giocatori")
        self.assertEqual(self.lobby.max_giocatori, 2)  # Singolo
        self.lobby.tipo_partita = 'Doppio'
        self.assertEqual(self.lobby.max_giocatori, 4)  # Doppio

    def test_aggiungi_giocatore(self):
        print("Test aggiunta giocatore")
        self.lobby.aggiungi_giocatore(self.user)
        self.assertEqual(self.lobby.numero_giocatori, 2)

    def test_rimuovi_giocatore(self):
        print("Test rimozione giocatore")
        self.lobby.rimuovi_giocatore(self.user)
        self.assertEqual(self.lobby.numero_giocatori, 0)

    def tearDown(self):
        self.user.delete()
        self.prenotazione.delete()
        self.lobby.delete()




