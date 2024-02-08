from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('impostazioni/', views.impostazioni, name='impostazioni'),
    path('modifica_profilo',views.modifica_profilo, name='modifica_profilo'),
    path('aggiungiindirizzo',views.aggiungi_indirizzo, name='aggiungi_indirizzo'),
    path('rimuoviindirizzo/<int:indirizzo_id>/', views.rimuovi_indirizzo, name='rimuovi_indirizzo')

]
