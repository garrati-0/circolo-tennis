from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):

    return render(request, 'home.html')






def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Modifica da 'email' a 'username'
        password = request.POST.get('password')
        
        # Usa il gestore personalizzato per l'autenticazione
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            #messages.success(request, 'Accesso effettuato con successo.')
            return redirect('home')
        else:
            messages.error(request, 'Credenziali non valide. Riprova.')

    return redirect('home')





def register_view(request):
    if request.method == 'POST':
        new_firstname = request.POST.get('new_firstname')
        new_lastname = request.POST.get('new_lastname')
        new_email = request.POST.get('new_email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Verifica se l'email è unica
        if User.objects.filter(email=new_email).exists():
            messages.error(request, 'Questa email è già registrata. Scegli un\'altra email.')
            return redirect('home')  # Puoi modificare questa riga in base alla tua logica di reindirizzamento

        # Verifica se le password corrispondono
        if new_password != confirm_password:
            messages.error(request, 'Le password non corrispondono. Riprova.')
            return redirect('home')  # Puoi modificare questa riga in base alla tua logica di reindirizzamento

        # Verifica se l'username è unico
        new_username = f"{new_firstname.lower()}.{new_lastname.lower()}"
        if User.objects.filter(username=new_username).exists():
            messages.error(request, 'Questo username è già in uso. Scegline un altro.')
            return redirect('home')  # Puoi modificare questa riga in base alla tua logica di reindirizzamento

        # Crea un nuovo utente
        new_user = User.objects.create_user(
            username=new_username,
            first_name=new_firstname,
            last_name=new_lastname,
            email=new_email,
            password=new_password
        )
        login(request, new_user)
        messages.success(request, 'Registrazione effettuata con successo.')
        subject = 'Conferma Ordine'
        message = render_to_string('email.html', {'user': new_user,})
        plain_message = strip_tags(message)

        from_email = 'proovvvvvvvvvv@gmail.com'
        
        to_email = [new_user.email]

        send_mail(subject, plain_message, from_email, to_email, html_message=message)
        return redirect('home')  # Puoi modificare questa riga in base alla tua logica di reindirizzamento

    return redirect('home')  # Puoi modificare questa riga in base alla tua logica di reindirizzamento



def logout_view(request):
    logout(request)
    return redirect('home')  # Puoi modificare questa riga in base alla tua logica di reindirizzamento dopo il logout
