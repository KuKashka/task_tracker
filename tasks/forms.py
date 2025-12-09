from django import forms
from .models import Task  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  
        fields = ['title', 'description', 'deadline', 'status', 'priority']

    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})