from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('to do', 'To Do'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=100, verbose_name="Назва завдання")
    description = models.TextField(verbose_name="Опис завдання", blank=True, null=True) 
    deadline = models.DateTimeField(verbose_name="Крайній термін", blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, verbose_name="Task Status", default='to do')
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=20, verbose_name="Task Priority", default='low')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Coment(models.Model):
    content = models.TextField(verbose_name="Коментар")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    media = models.FileField(upload_to='comments_media/', blank=True, null=True)
    def __str__(self):
        return f'Comment by {self.author} on {self.task}'