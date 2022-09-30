from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
# Create your views here.


class TaskListView(ListView):
    model = Task

class TaskDetailView(DetailView):
    model = Task    
    context_object_name = 'task'
    
class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task-list')
    
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')