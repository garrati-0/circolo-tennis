from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from prodotti.models import Product
from django.contrib import messages
from prodotti.models import Preferiti
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
# Create your views here.
def contattacci(request):
    num = Preferiti.objects.filter(user=request.user).count()
    context = {
        'num': num,
    }

    return render(request, 'contattacci.html', context)

  
from django.shortcuts import render
  
from django.core.exceptions import ValidationError

def email(request):
    if request.method == 'POST':
        subject = 'Conferma Ordine'
        email = request.POST.get('email')
        message = render_to_string('emailmm.html', {
            'name': request.POST.get('name'),
            'email': email,
            'message': request.POST.get('message'),
            
        })
        
        plain_message = strip_tags(message)
        from_email = 'proovvvvvvvvvv@gmail.com'
        to_email = [email]
        
        send_mail(subject, plain_message, from_email, to_email, html_message=message)
        
        lain_message = strip_tags(message)
        from_email = 'proovvvvvvvvvv@gmail.com'
        to_email = ['proovvvvvvvvvv@gmail.com']
        messages.success(request, 'Email inviata con successo.')
        send_mail(subject, plain_message, from_email, to_email, html_message=message)
        return redirect('contattacci')
    messages.error(request, 'Errore nell\'invio dell\'email.')
    return redirect('contattacci')
