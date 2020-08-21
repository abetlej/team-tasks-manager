from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'deadline', 'completed']
        labels = {'description': 'task', 'deadline' : 'deadline', 'completed' : 'completed'}