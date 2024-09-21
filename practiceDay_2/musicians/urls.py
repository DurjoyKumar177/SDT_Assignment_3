from django.urls import path
from . import views

urlpatterns = [
    path('add-musician/', views.create_musician, name='add_musician'),
    path('edit-musician/<int:musician_id>/', views.edit_musician, name='edit_musician'),
    path('delete-musician/<int:musician_id>/', views.delete_musician, name='delete_musician'),
]
