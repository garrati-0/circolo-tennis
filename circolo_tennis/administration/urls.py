from django.urls import path
from .views import login_view, administration, administration_dashboard
from django.urls import path
from . import views

urlpatterns = [
    path('', login_view, name='login'),
    path('administration_if/', administration, name='administration'),
    path('administration/dashboard/', administration_dashboard, name='administration_dashboard'),
    path('administration/prodotti/', views.aggiungi_prodotto, name='aggiungi_prodotto'),
    path('update_quantities/', views.update_quantita, name='update_quantita'),
    # Altri URL del tuo progetto...
]