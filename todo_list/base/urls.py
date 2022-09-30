from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list' ),
    path('task-detail/<int:pk>/', views.TaskDetailView.as_view(), name="task-detail"),
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
]