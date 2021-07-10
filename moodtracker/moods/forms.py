from django import forms
from . import models

class NewMood(forms.ModelForm):
    class Meta:
        model = models.Mood
        fields = ['rating', 'comment']
