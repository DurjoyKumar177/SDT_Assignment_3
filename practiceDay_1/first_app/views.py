from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.

def html_form(request):
    return render(request, 'html_form.html')

def django_form(request):
    form = ExampleForm()
    return render(request, 'django_form.html', {'form':form})

