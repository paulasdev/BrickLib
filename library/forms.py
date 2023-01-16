from django import forms
from .models import Set


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = [
            'theme',
            'title',
            'description',
            'done',
            'featured_image',
        ]
        label = {
            'theme': '',
            'title': '',
            'description': '', 
            'done': '',
        }
        widgets = { 
            'title': forms.TextInput(attrs={'placeholder': 'Bricks & Sets'}),
            'description': forms.TextInput(attrs={'placeholder': 'e.g. Color, Year, Details'}),
        }