from django import forms
from .models import Task  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  
        fields = ['title', 'description', 'deadline', 'status', 'priority', 'author']

    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

class TaskCreateView(update.view):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'priority', 'author']

    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)