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
            'theme': '',
            'name': '',
            'description': '', 
            'done': '',
        }
        widgets = { 
            'name': forms.TextInput(attrs={'placeholder': 'Bricks & Sets'}),
            'description': forms.TextInput(attrs={'placeholder': 'e.g. Color, Year, Details'}),
        }