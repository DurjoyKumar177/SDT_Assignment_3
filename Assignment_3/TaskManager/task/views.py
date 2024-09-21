from django.shortcuts import render, redirect
from .models import TaskModel
from . import forms

# # Create your views here.



def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save()  # Save the task first            
            return redirect('show_tasks')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form': task_form})

def edit_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = forms.TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    task.delete()
    return redirect('show_tasks')

def complete_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')

