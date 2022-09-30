from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
# Create your views here.


class TaskListView(ListView):
    model = Task

class TaskDetailView(DetailView):
    model = Task    
    context_object_name = 'task'