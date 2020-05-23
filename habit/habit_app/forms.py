from django import forms
from datetime import date

from .models import Habit, Progress


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'title', 'description', 'start_date', 'reason', 'plan']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yy-mm-dd', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'plan': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'})

        }


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['rating', 'edit_date', 'feeling']
        CHOICES = [(i, i) for i in range(11)]
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES),
            'edit_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yy-mm-dd', 'type': 'date'}),
            'feeling': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'})
        }
