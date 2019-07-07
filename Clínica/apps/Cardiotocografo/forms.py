from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = [
            'codigo',
            'enfermedad_padecida',
            'enfermedad_hereditarias',
        ]

        labels = {
            'codigo': 'Código',
            'enfermedad_padecida': 'Enfermedad padecida',
            'enfermedad_hereditarias': 'Enfermedades hereditarias',
        }