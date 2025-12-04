from django.shortcuts import render
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task # Припустимо, у вас є модель Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'priority', 'author']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

    def formw_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        # Додаткові дії після валідації форми, якщо потрібно
        return super().form_valid(form)