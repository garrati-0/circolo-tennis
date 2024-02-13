from django.urls import path
from . import views

urlpatterns = [
    path('prodotti/<str:categoria>/', views.prodotti, name='prodotti'),
    path('aggiungi_ai_preferiti/<int:prodotto_id>/', views.aggiungi_ai_preferiti, name='aggiungi_ai_preferiti'),
    path('inserisci_recensione/<int:prodotto_id>/', views.inserisci_recensione, name='inserisci_recensione'),
]