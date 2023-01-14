from django import forms
from .models import Set


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = [
            'theme',
            'name',
            'description',
            'done',
            'featured_image',
        ]
        label = {
            'theme': 'Theme Set',
            'name': 'Brick / Set name',
            'description': 'ex. Number of pcs, color,', 
            'done': '',
        }
        widgets = { 
            'name': forms.TextInput(attrs={'placeholder': 'Bricks & Sets'}),
            'description': forms.TextInput(attrs={'placeholder': 'e.g. Color, Year, Details'}),
        }