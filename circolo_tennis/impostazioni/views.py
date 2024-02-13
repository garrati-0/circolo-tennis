from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Indirizzo, UserProfile
import os
import requests
from django.contrib import messages
from os.path import basename
from django.contrib.auth.decorators import login_required
# Create your views here.

from django import forms


@login_required
def impostazioni(request):
    # Assicura che l'utente sia autenticato prima di procedere
    if request.user.is_authenticated:
        # Recupera gli indirizzi dell'utente loggato
        indirizzi = Indirizzo.objects.filter(user=request.user)
        return render(request, 'impostazioni.html', {'indirizzi': indirizzi})
    else:
        # In caso di utente non autenticato, reindirizza alla pagina di accesso
        return redirect('home.html')  # Assicurati di sostituire 'pagina_login' con il nome reale della tua pagina di accesso


def validate_address(via, civico, cap, citta, provincia, stato):
    # Costruisci l'indirizzo completo
    indirizzo_completo = f"{via}, {civico}, {cap} {citta}, {provincia}, {stato}"

    # Sostituisci gli spazi con '+'
    indirizzo_completo = indirizzo_completo.replace(' ', '+')

    # Aggiungi la tua chiave API di Google Maps
    api_key = 'AIzaSyB5xOjYbhn0Kzy68H9d38pOc1AX5MknEN4'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={indirizzo_completo}&key={api_key}'

    # Fai una richiesta alle API di Google Maps
    response = requests.get(url)
    data = response.json()

    # Verifica se l'indirizzo è valido
    if data['status'] == 'OK':
        # Puoi aggiungere ulteriori controlli qui se necessario
        return True
    else:
        return False

def aggiungi_indirizzo(request):
    if request.method == 'POST':
        via = request.POST.get('via')
        civico = request.POST.get('civico')
        cap = request.POST.get('cap')
        citta = request.POST.get('citta')
        provincia = request.POST.get('provincia')
        stato = request.POST.get('stato')

        # Valida l'indirizzo utilizzando le API di Google
        if validate_address(via, civico, cap, citta, provincia, stato):
            # Recupera l'utente loggato o in base alle tue esigenze
             # Recupera l'utente loggato o in base alle tue esigenze
            user = request.user

    # Crea una nuova istanza dell'oggetto Indirizzo e salvalo nel database
            indirizzo = Indirizzo(via=via, civico=civico, cap=cap, citta=citta, provincia=provincia, stato=stato, user=user)
            indirizzo.save()
          

            # Puoi aggiungere ulteriori controlli o reindirizzamenti qui
            return redirect('impostazioni')  # Cambia 'pagina_di_destinazione' con l'URL desiderato
    messages.error(request, 'Indirizzo non valido. Riprova.')
    return redirect('impostazioni')  # Assicurati di avere un template per il popup


def rimuovi_indirizzo(request, indirizzo_id):
    # Recupera l'istanza dell'indirizzo da rimuovere
    indirizzo = get_object_or_404(Indirizzo, id=indirizzo_id)
    print(indirizzo)
    if request.method == 'POST':
        # Se la richiesta è una POST, conferma la rimozione
        indirizzo.delete()
          # Sostituisci 'settings' con il nome della tua vista di modifica profilo
    return redirect('impostazioni')
    
    


from os.path import basename
from django.contrib import messages
from django.shortcuts import redirect
from .models import UserProfile

def modifica_profilo(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        # Estrai i dati dalla richiesta POST
        foto_profilo = request.FILES.get('profileimage')
        new_password = request.POST.get('changepassword')

        # Aggiorna l'immagine del profilo se presente
        if foto_profilo:
            # Estrai solo il nome del file dall'URL
            nome_file = basename(foto_profilo.name)

            # Salva solo il nome del file senza il percorso completo
            user_profile.foto_profilo.save(nome_file, foto_profilo)
            user_profile.nomefoto = nome_file

        # Cambia la password solo se è stata fornita
        if new_password:
            request.user.set_password(new_password)
            request.user.save()

        user_profile.save()
        messages.success(request, 'Le modifiche sono state salvate con successo.')
        return redirect('impostazioni')

    return redirect('impostazioni')
