from django import forms
from . import models

class NewMood(forms.ModelForm):
    class Meta:
        model = models.Mood
        fields = ['date', 'rating', 'comment', 'positives', 'negatives']

class TodayMood(forms.ModelForm):
    class Meta:
        model = models.Mood
        fields = ['rating', 'comment', 'positives', 'negatives']
