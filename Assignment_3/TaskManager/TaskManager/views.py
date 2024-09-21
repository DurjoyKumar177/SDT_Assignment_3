from django.shortcuts import render, redirect
from task.models import TaskModel

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})