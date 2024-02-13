from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Preferiti
from .forms import RecensioneForm


def prodotti(request,categoria):
    user = request.user
    myproduct = Product.objects.filter(categoria=categoria).prefetch_related('recensioni')
    num = Preferiti.objects.filter(user=request.user).count()

    
    context = {
        'categoria': categoria,
        'prodotti': prodotti
    }
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
        'num': num,
    }
    return render(request, 'prodotti.html', context)

@login_required
def aggiungi_ai_preferiti(request, prodotto_id):
    prodotto = get_object_or_404(Product, id=prodotto_id)

    #if not Preferiti.objects.filter(user=request.user, prodotto=prodotto).exists():
    preferiti = Preferiti.objects.create(user=request.user, prodotto=prodotto)
    counter = preferiti.increment_counter()
    messages.success(request, "Prodotto aggiunto ai preferiti.")
    #else:
       # messages.error(request, "Prodotto già presente nei preferiti.")

    return redirect('prodotti', categoria=prodotto.categoria)    
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

    return redirect('prodotti', categoria=prodotto.categoria)    
