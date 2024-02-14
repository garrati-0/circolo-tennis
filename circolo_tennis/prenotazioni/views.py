from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

from prodotti.models import Preferiti
from .models import PrenotazioneCampo
from django.utils.translation import activate
from django.utils.dateparse import parse_date
from datetime import date, datetime, timedelta
from django.shortcuts import render, redirect
from django.utils.translation import activate
from .models import PrenotazioneCampo
from .models import Lobby
from django.contrib import messages


def prenotazioni(request, data_selezionata=None):
    
    if data_selezionata is None:
        data_selezionata = date.today()
    else:
        data_selezionata = datetime.strptime(data_selezionata, '%Y-%m-%d').date()

    ora_attuale = datetime.now().time()

   
    activate('it')

    prenotazioni_oggi = PrenotazioneCampo.objects.filter(data=data_selezionata, orario__gte=ora_attuale).order_by('campo', 'orario')

    
    # Calcola la data per il giorno successivo e precedente
    data_successiva = data_selezionata + timedelta(days=1)
    data_precedente = data_selezionata - timedelta(days=1)
    if request.user.is_authenticated:
        num = Preferiti.objects.filter(user=request.user).count()
        return render(request, 'prenotazioni.html', {
        'prenotazioni': prenotazioni_oggi,
        'data_selezionata': data_selezionata,
        'data_successiva': data_successiva,
        'data_precedente': data_precedente,
        'num': num,
        })
    return render(request, 'prenotazioni.html', {
        'prenotazioni': prenotazioni_oggi,
        'data_selezionata': data_selezionata,
        'data_successiva': data_successiva,
        'data_precedente': data_precedente,
        })



def crea_prenotazioni_settimanali(request):
    PrenotazioneCampo.objects.all().delete()
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
                    cliente=request.user,
                    settimana=settimana_corrente,
                    durata=durata_prenotazione
                )
                # Incrementa l'orario di prenotazione di 1 ora
                orario_prenotazione = (datetime.combine(date.min, orario_prenotazione) + timedelta(hours=1)).time()

    return redirect('administration_dashboard')



def cancella_tutte_prenotazioni(request):
    PrenotazioneCampo.objects.all().delete()
    return redirect('administration_dashboard') 



def prenotazioni_data(request, data_selezionata=None):
    # Se data_selezionata è None, imposta la data corrente
    if data_selezionata is None:
        data_selezionata = datetime.now().date()
    else:
        # Converte la data selezionata in un oggetto datetime
        data_selezionata = parse_date(data_selezionata)
        if data_selezionata is None:
            # La data selezionata non è valida, puoi gestire questo caso a tuo piacimento
            # Ad esempio, puoi restituire una risposta di errore o impostare una data predefinita
            return HttpResponse("Data selezionata non valida")

    activate('it')
    prenotazioni_oggi = PrenotazioneCampo.objects.filter(data=data_selezionata).order_by('campo', 'orario')

    # Calcola la data per il giorno successivo e precedente
    data_successiva = data_selezionata + timedelta(days=1)
    data_precedente = data_selezionata - timedelta(days=1)

    return render(request, 'prenotazioni.html', {
        'prenotazioni': prenotazioni_oggi,
        'data_selezionata': data_selezionata,
        'data_successiva': data_successiva,
        'data_precedente': data_precedente,
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import PrenotazioneCampo

def conferma_prenotazione(request, prenotazione_id):
   
    

    # Recupera la prenotazione dal database
    prenotazione = get_object_or_404(PrenotazioneCampo, id=prenotazione_id)

   
    
    # Verifica che la prenotazione non sia già stata confermata
    if not prenotazione.prenotato:
        # Aggiorna il campo 'prenotato'
        prenotazione.cliente = request.user
        prenotazione.prenotato = True
        prenotazione.save()
        messages.success(request, 'Prenotazione confermata con successo.')
       
        return redirect('prenotazioni')
    messages.error(request, 'Errore nella conferma della prenotazione.')
 
    return redirect('prenotazioni')


@login_required
def mie_prenotazioni(request):
    num = Preferiti.objects.filter(user=request.user).count()
    user = request.user
    prenotazioni_utente = PrenotazioneCampo.objects.filter(cliente=user).order_by('data', 'orario')

    return render(request, 'mie_prenotazioni.html', {'prenotazioni_utente': prenotazioni_utente, 'num': num})






def visualizza_lobbies(request):
    # Recupera tutte le lobby dal database
    num = Preferiti.objects.filter(user=request.user).count()
    tutte_le_lobbies = Lobby.objects.all()
    for x in tutte_le_lobbies:
        print(x.partecipanti.all())
   
    return render(request, 'lobby.html', {'tutte_le_lobbies': tutte_le_lobbies, 'num': num})




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lobby, PrenotazioneCampo

@login_required
def crea_lobby(request, prenotazione_id):
    print("Crea lobby")
    if request.method == 'POST':
        print("Post")
        tipo_partita = request.POST.get('tipo_partita')
        livello = request.POST.get('livello')
        creator = request.user
        
        
        prenotazione = get_object_or_404(PrenotazioneCampo, id=prenotazione_id)
        print("Post")

        
   
    
    # Verifica che la prenotazione non sia già stata confermata
        if not prenotazione.prenotato:
        # Aggiorna il campo 'prenotato'
            prenotazione.cliente = request.user
            prenotazione.prenotato = True
            prenotazione.save()  # ID della prenotazione del campo

        # Ottieni l'istanza della prenotazione del campo
        prenotazione_campo = PrenotazioneCampo.objects.get(id=prenotazione_id)
        
        # Crea una nuova istanza di Lobby nel database
        lobby = Lobby.objects.create(
            tipo_partita=tipo_partita,
            livello=livello,
            creator=creator,
            prenotazione_campo=prenotazione_campo,  # Assegna la prenotazione del campo alla lobby
            pubblicata=True
        )
        messages.success(request, 'Lobby creata con successo.')
       
        return redirect('prenotazioni')  #
    messages.error(request, 'Errore nella creazione della lobby.') 
    return redirect('prenotazioni') 



def aggiungi_giocatore(request, lobby_id):
    # Ottieni la lobby dalla richiesta
    lobby = get_object_or_404(Lobby, id=lobby_id)
    print(lobby)
    # Verifica se l'utente è autenticato
    if request.user.is_authenticated:
        # Controlla se la lobby ha ancora posti disponibili
        print(lobby.numero_giocatori)
        print(lobby.max_giocatori)
        if lobby.numero_giocatori < lobby.max_giocatori:
            lobby.numero_giocatori= lobby.numero_giocatori + 1
            lobby.partecipanti.add(request.user)
            lobby.save()
            print(lobby.numero_giocatori)
            print(lobby.partecipanti.all())
            messages.success(request, 'Sei stato aggiunto alla lobby con successo.')
            # Verifica se il numero di giocatori è uguale al massimo consentito
            if lobby.numero_giocatori == lobby.max_giocatori:
                # Imposta la lobby come non pubblicata
                lobby.pubblicata = False
                lobby.save()
            return redirect('visualizza_lobbies')
    messages.error(request, 'La lobby è già al completo.')
    # Ritorna alla pagina della lobby dopo l'aggiunta del giocatore
    return redirect('visualizza_lobbies')  




def le_mie_lobbies(request):
    num = Preferiti.objects.filter(user=request.user).count()
    # Ottieni le lobby create dall'utente corrente
    lobbies_create = Lobby.objects.filter(creator=request.user)

    # Ottieni le lobby alle quali partecipa l'utente corrente
    lobbies_partecipate = request.user.partecipated_lobbies.all()

    context = {
        'lobbies_create': lobbies_create,
        'lobbies_partecipate': lobbies_partecipate,
        'num': num,
    }

    return render(request, 'le_tue_lobby.html', context)