from django import forms
from .models import Plant, CareLog

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            'name', 
            'species', 
            'photo', 
            'location', 
            'irrigation_frequency'
        ]

class CareLogForm(forms.ModelForm):
    class Meta:
        model = CareLog
        fields =[
            'date',
            'watered',
            'fertilized',
            'notes'
        ]
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
