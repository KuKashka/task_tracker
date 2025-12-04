from django.urls import path
from .views import*

urlpatterns = [
    
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
]