from django import forms
from .models import Timeline, Project

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter timeline name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter timeline description'}),
        }

class ProjectForm(forms.ModelForm):
    clock_length = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in [2, 4, 6, 8, 10, 12, 16, 20]],
        coerce=int,
        initial=4,
        label='Total Length'
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'factions']
        widgets = {
            'factions': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Existing instance; remove clock_length field
            self.fields.pop('clock_length')
