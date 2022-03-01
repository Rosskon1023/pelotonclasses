from nis import cat
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Class, Artist
from .forms import ArtistForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def classes_index(request):
    classes = Class.objects.all()
    return render(request, 'classes/index.html', {'classes': classes})

def classes_detail(request, class_id):
    pelclass = Class.objects.get(id=class_id)
    artist_form = ArtistForm()

    return render(request, 'classes/detail.html', {
        'class': pelclass,
        'artist_form': artist_form
    })

def add_artist(request, class_id):
    form = ArtistForm(request.POST)
    if form.is_valid():
        new_artist = form.save(commit=False)
        new_artist.pelclass_id = class_id
    new_artist.save()
    return redirect('detail', class_id=class_id)




class ClassCreate(CreateView):
    model = Class
    fields = '__all__'

class ClassDelete(DeleteView):
    model = Class
    success_url = '/classes/'

class ClassUpdate(UpdateView):
    model = Class
    fields = '__all__'

