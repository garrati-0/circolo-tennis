from django import forms
from .models import Product, Recensione

class RecensioneForm(forms.ModelForm):
    class Meta:
        model = Recensione
        fields = ['testo', 'voto']