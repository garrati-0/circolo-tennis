from django.urls import path
from . import views

urlpatterns = [
    path('', views.prenotazioni, name='prenotazioni'),
    path('crea_prenotazioni_settimanali/', views.crea_prenotazioni_settimanali, name='crea_prenotazioni_settimanali'),
    path('cancella_tutte_prenotazioni/', views.cancella_tutte_prenotazioni, name='cancella_tutte_prenotazioni'),
    # Aggiungi una nuova vista che permetta di navigare avanti e indietro tra i giorni
    path('prenotazioni/<str:data_selezionata>/', views.prenotazioni_data, name='prenotazioni_data'),
    path('conferma_prenotazione/<int:prenotazione_id>/', views.conferma_prenotazione, name='conferma_prenotazione'),
    path('mie_prenotazioni/', views.mie_prenotazioni, name='mie_prenotazioni'),
    path('visualizza_lobbies/', views.visualizza_lobbies, name='visualizza_lobbies'),   
    path('prenotazioni/crea_lobby/<int:prenotazione_id>/', views.crea_lobby, name='crea_lobby'),
    path('aggiungi_giocatore/<int:lobby_id>/', views.aggiungi_giocatore, name='aggiungi_giocatore'),
    path('mie-lobbies/', views.le_mie_lobbies, name='mie_lobbies'),
]
