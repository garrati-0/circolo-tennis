from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Indirizzo, OrdineEffettuato
from prodotti.models import Preferiti, Product
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@login_required
def carrello(request):
    user = request.user
    myproducts = Preferiti.objects.filter(user=user).select_related('prodotto')
    costo_totale = myproducts.aggregate(Sum('prodotto__prezzo'))['prodotto__prezzo__sum'] or 0
    indirizzi = Indirizzo.objects.filter(user=user)
    print(myproducts)
    template = loader.get_template('carrello.html')
    context = {
        'myproducts': myproducts,
        'user': user,
        'costo_totale': costo_totale,
        'indirizzi': indirizzi
    }
    return HttpResponse(template.render(context, request))

@login_required
def rimuovi(request, prodotto_id):
    user = request.user
    Preferiti.objects.filter(user=user, prodotto_id=prodotto_id).delete()
    return redirect('carrello')

@login_required
def ordine_effetuato(request):
    user = request.user
    indirizzo_id = request.POST.get('selected_address')
    indirizzo_selezionato = Indirizzo.objects.get(id=indirizzo_id)
    prodotti_preferiti = Preferiti.objects.filter(user=user)

    costo_totale = prodotti_preferiti.aggregate(Sum('prodotto__prezzo'))['prodotto__prezzo__sum'] or 0
    prodotti_ordine = []

    for preferito in prodotti_preferiti:
        prodotto_selezionato = preferito.prodotto

        if prodotto_selezionato.quantita > 0:
            prodotto_selezionato.quantita -= 1
            prodotto_selezionato.save()

        ordine = OrdineEffettuato.objects.create(
            id_utente=user,
            id_indirizzo=indirizzo_selezionato,
            id_prodotto=prodotto_selezionato
        )

        prodotti_ordine.append(prodotto_selezionato)

    subject = 'Conferma Ordine'
    message = render_to_string('email.html', {'user': user, 'ordine': ordine, 'prodotti_ordine': prodotti_ordine})
    plain_message = strip_tags(message)

    from_email = 'proovvvvvvvvvv@gmail.com'
    to_email = [user.email]

    send_mail(subject, plain_message, from_email, to_email, html_message=message)

    prodotti_preferiti.delete()
    return redirect('carrello')
