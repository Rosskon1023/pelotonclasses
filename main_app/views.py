from django.shortcuts import render
from .models import Class


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def classes_index(request):
    classes = Class.objects.all()
    return render(request, 'classes/index.html', {'classes': classes})