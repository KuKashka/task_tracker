from django.shortcuts import render
from .forms import TaskForm
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Task # Припустимо, у вас є модель Task
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AuthorRequiredMixin


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    def get_queryset(self):
        tasks = Task.objects.filter(author=self.request.user)
        status_filter = self.request.GET.get('status_filter')
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        return tasks

class TaskDetailView(AuthorRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        # Додаткові дії після валідації форми, якщо потрібно
        return super().form_valid(form)

class TaskUpdateView(AuthorRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_edit.html'
    success_url = reverse_lazy('home')

class TaskDeleteView(AuthorRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('home')
