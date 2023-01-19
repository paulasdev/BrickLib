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
            'theme': forms.Select(attrs={'class' : 'form-control'}),
            'title': forms.TextInput(attrs={'class' : 'form-control', 
                                    'placeholder': 'Bricks & Sets'}),
            'description': forms.Textarea(attrs={'class' : 'form-control', 
                                        'placeholder': 'e.g. color, year, details'}),
        }