from django import forms
from .models import TaskModel
from catagory.models import TaskCategory

class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=TaskCategory.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed', 'categories']  # Include the categories field
