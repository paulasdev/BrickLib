from django import forms
from .models import Set


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = [
            'theme',
            'title',
            'description',
            'featured_image',
        ]
        label = {
            'theme': '',
            'title': '',
            'description': '', 
            'fearured_image': '',
        }
        widgets = { 
            'theme': forms.Select(attrs={'class' : 'form-control'}),
            'title': forms.TextInput(attrs={'class' : 'form-control', 
                                    'placeholder': 'Bricks & Sets'}),
            'description': forms.Textarea(attrs={'class' : 'form-control', 
                                        'placeholder': 'e.g. color, year, details'}),
        }