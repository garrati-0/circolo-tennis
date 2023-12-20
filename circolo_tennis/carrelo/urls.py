from django.urls import path
from . import views

urlpatterns = [
    path('carrello', views.carrello, name='carrello'),
    path('rimuovi/<int:prodotto_id>/', views.rimuovi, name='rimuovi'),
    path('ordine_effetuato', views.ordine_effetuato, name='ordine_effetuato'),

]