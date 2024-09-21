from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add-task/', views.add_task, name='add_task'),
    path('show-tasks/', views.show_tasks, name='show_tasks'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete-task/<int:task_id>/', views.complete_task, name='complete_task'),
]
