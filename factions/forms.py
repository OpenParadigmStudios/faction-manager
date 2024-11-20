from django import forms
from .models import Game, Project

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter game name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter game description'}),
        }

class ProjectForm(forms.ModelForm):
    length = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in [2, 4, 6, 8, 10, 12, 16, 20]],
        coerce=int,
        initial=4,
        label='Total Length'
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'factions', 'length']
        widgets = {
            'factions': forms.CheckboxSelectMultiple(),
        }
