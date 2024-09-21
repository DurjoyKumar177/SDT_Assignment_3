from django.shortcuts import render, redirect, get_object_or_404
from .models import Musician
from .forms import MusicianForm

# Create Musician
def create_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm()
    return render(request, 'musician_form.html', {'form': form})

# Edit Musician
def edit_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musician_form.html', {'form': form})

# Delete Musician
def delete_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    musician.delete()
    return redirect('homepage')
