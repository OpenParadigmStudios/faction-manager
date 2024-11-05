from django import forms
from .models import Timeline

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter timeline name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter timeline description'}),
        }
