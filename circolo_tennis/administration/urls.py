from django.urls import path
from .views import login_view, administration, administration_dashboard
from django.urls import path
from . import views

urlpatterns = [
    path('', login_view, name='administartion'),
    path('administration_if/', administration, name='administration'),
    path('administration/dashboard/', administration_dashboard, name='administration_dashboard'),
    path('administration/prodotti/', views.aggiungi_prodotto, name='aggiungi_prodotto'),
    path('update_quantities/', views.update_quantita, name='update_quantita'),
    path('crea_prenotazioni_settimanali/', views.crea_prenotazioni_settimanali, name='crea_prenotazioni_settimanali'),
    path('cancella_tutte_prenotazioni/', views.cancella_tutte_prenotazioni, name='cancella_tutte_prenotazioni'),
    # Altri URL del tuo progetto...
]