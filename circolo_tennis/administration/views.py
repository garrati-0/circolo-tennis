from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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
    # Vista della dashboard di amministrazione
    return render(request, 'administration_dashboard.html')
