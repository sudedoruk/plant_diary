from django import forms
<<<<<<< HEAD
from .models import Plant, CareLog
=======
from .models import Plant
>>>>>>> 7160f4d21e2332bebb61782cb3b7a70d4d89e490

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            'name', 
            'species', 
            'photo', 
            'location', 
            'irrigation_frequency'
<<<<<<< HEAD
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
=======
        ]
>>>>>>> 7160f4d21e2332bebb61782cb3b7a70d4d89e490
