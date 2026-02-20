from django import forms
from django.core.exceptions import ValidationError
import re
from core.models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','email','mensaje']

    # Validación de Backend
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@utez.edu.mx" not in data:
            raise ValidationError("Solo puedes registrar correos de la utez")
        return data
    
    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if not re.match('^[a-zA-Z]+$',data):
            raise ValidationError("Solo puedes registrar nombres con letras")
        return data