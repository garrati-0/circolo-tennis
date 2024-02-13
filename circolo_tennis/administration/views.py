from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from carrelo.models import OrdineEffettuato
from prodotti.models import Product
import json
from prenotazioni.models import PrenotazioneCampo 
import os
from datetime import date, datetime, timedelta


def login_view(request):
    if request.user.is_authenticated:
        # Se l'utente è già autenticato, reindirizza alla pagina di amministrazione
        if request.user.is_superuser:
            return redirect('administration_dashboard')
        else:
            return redirect('administration')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticazione dell'utente
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            # Login dell'utente superuser
            login(request, user)
            return redirect('administration_dashboard')  # Reindirizzamento alla pagina di amministrazione dopo il login
        
        elif user is not None:
            # Login dell'utente non superuser
            login(request, user)
            return redirect('administration')

        else:
            # Credenziali non valide
            error_message = "Credenziali non valide."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Metodo GET, quindi mostra la pagina di login
        return render(request, 'login.html')




@login_required
def administration(request):
    if request.user.is_superuser:
        # L'utente è autenticato ed è un superuser (root)
        return redirect('administration_dashboard')  # Assumi che 'administration_dashboard' sia l'URL della pagina di amministrazione
    else:
        # L'utente è autenticato ma non è un superuser
        error_message = "Non sei autorizzato ad accedere a questa pagina."
        return render(request, 'error.html', {'error_message': error_message})





@login_required
def administration_dashboard(request):
    # Recupera tutti i prodotti
    
    prodotti = Product.objects.all()
    prenotazioni = PrenotazioneCampo.objects.all().order_by('data')
    ordini = OrdineEffettuato.objects.all()
    
    return render(request, 'administration_dashboard.html', {'prodotti': prodotti,'prenotazioni': prenotazioni, 'ordini': ordini}) 




def aggiungi_prodotto(request):
    if request.method == 'POST':
        new_product = request.POST.get('new_product')
        new_price = request.POST.get('new_price')
        new_image = request.FILES.get('new_image')
        new_info = request.POST.get('new_info')  # Aggiunto per ottenere le informazioni
        new_description = request.POST.get('new_description')  # Aggiunto per ottenere la descrizione
        
        new_image_name = new_image.name if new_image else None  # Ottieni il nome dell'immagine
        
        if new_product and new_price and new_image:
            prodotto = Product.objects.create(
                prodotto=new_product,
                prezzo=new_price,
                imagine=new_image,
                nomeimg=new_image_name,  # Salva il nome dell'immagine
                informazioni=new_info,
                descrizione=new_description
            )
            
            return redirect('administration_dashboard')  # Redirect alla pagina di successo dopo l'aggiunta del prodotto
            
    return redirect('administration_dashboard')  # Redirect alla pagina di successo dopo l'aggiunta del prodotto



def update_quantita(request):
    if request.method == 'POST':
        for prodotto in Product.objects.all():
            quantita_key = f'quantita_{prodotto.id}'
            if quantita_key in request.POST:
                new_quantita = request.POST[quantita_key]
                prodotto.quantita = new_quantita
                prodotto.save()

    return redirect('administration_dashboard')





def crea_prenotazioni_settimanali(request):
    
    oggi = date.today()
    settimana_corrente = oggi.isocalendar()[1]

    campi = {
        'Campo 1': {'orario_inizio': '06:00'},
        'Campo 2': {'orario_inizio': '06:15'},
        'Campo 3': {'orario_inizio': '06:30'},
    }

    durata_prenotazione = 1  # 1 ora di prenotazione

    for campo, config in campi.items():
        orario_inizio = datetime.strptime(config['orario_inizio'], '%H:%M').time()

        for giorno in range(7):
            data_prenotazione = oggi + timedelta(days=giorno)
            orario_prenotazione = orario_inizio

            while orario_prenotazione < datetime.strptime('23:00', '%H:%M').time():
                PrenotazioneCampo.objects.create(
                    campo=campo,
                    orario=orario_prenotazione,
                    data=data_prenotazione,
                    cliente=None,
                    settimana=settimana_corrente,
                    durata=durata_prenotazione
                )
                # Incrementa l'orario di prenotazione di 1 ora
                orario_prenotazione = (datetime.combine(date.min, orario_prenotazione) + timedelta(hours=1)).time()

    return redirect('administration_dashboard')



def cancella_tutte_prenotazioni(request):
    PrenotazioneCampo.objects.all().delete()
    return redirect('administration_dashboard')  # Sostituisci 'prenotazioni' con il nome corretto della tua vista