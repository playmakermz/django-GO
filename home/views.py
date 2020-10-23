from django.shortcuts import render, redirect
from .models import *

def home(request):
    note = Note.objects.all()

    if request.method == 'POST':
        form = Note(title=request.POST['title'])
        form.save()
        return redirect('/')

    main = {
        'note':note,
    }

    return render(request, 'home.html', main)

def update(request, pk):
    from .models import Note
    note = Note.objects.get(id=pk)

    if request.method == 'POST':
        form = request.POST['title']
        note.title = form
        note.save()
        return redirect ('/')

    main = {
        'note':note,
    }

    return render(request, 'edit.html', main)

def delete(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/')

    main = {
        'note':note,
    }
    return render(request, 'delete.html', main)
