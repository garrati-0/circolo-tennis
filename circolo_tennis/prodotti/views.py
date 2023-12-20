from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Preferiti
from .forms import RecensioneForm


def prodotti(request):
    user = request.user
    myproduct = Product.objects.all().prefetch_related('recensioni')
    order = request.GET.get('order', 'price_asc')

    # Define the sorting order based on the 'order' parameter
    if order:
        if order == 'price_asc':
            myproduct = myproduct.order_by('prezzo')
        elif order == 'price_desc':
            myproduct = myproduct.order_by('-prezzo')
    context = {
       
        'user': user,
        'myproduct': myproduct,
    }
    return render(request, 'prodotti.html', context)

@login_required
def aggiungi_ai_preferiti(request, prodotto_id):
    prodotto = get_object_or_404(Product, id=prodotto_id)

    if not Preferiti.objects.filter(user=request.user, prodotto=prodotto).exists():
        preferiti = Preferiti.objects.create(user=request.user, prodotto=prodotto)
        messages.success(request, "Prodotto aggiunto ai preferiti.")
    else:
        messages.error(request, "Prodotto già presente nei preferiti.")

    return redirect('home')  # Modifica se necessario

@login_required
def inserisci_recensione(request, prodotto_id):
    prodotto = get_object_or_404(Product, id=prodotto_id)

    if request.method == 'POST':
        form = RecensioneForm(request.POST)
        if form.is_valid():
            recensione = form.save(commit=False)
            recensione.utente = request.user
            recensione.save()
            prodotto.recensioni.add(recensione)
            messages.success(request, "Recensione inserita con successo.")
        else:
            messages.error(request, "Errore nella validazione del form.")

    return redirect('prodotti')  # Modifica se necessario
