from django import forms
from .models import Project

# Meta is an inner class used to give configuration/settings to the outer class.

class ProjectForm(forms.ModelForm):
    class Meta: 
        model = Project
        fields = ['topic', 'languages_used', 'duration']
        widgets = {
            'topic': forms.TextInput(attrs={'placeholder': 'Enter project topic'}),
            'languages_used': forms.Textarea(attrs={'placeholder': 'Enter languages used'}),
            'duration': forms.NumberInput(attrs={'placeholder': 'Enter duration in weeks'}),
        }
        labels = {
            'topic': 'Project Topic',
            'languages_used': 'Languages Used for the Project',
            'duration': 'Duration (Weeks)',
        }
