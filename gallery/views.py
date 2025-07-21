from re import M
from django.shortcuts import render
from .models import Photo


def index(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/index.html', {'cards': photos})


def show(request, id):
    photo = Photo.objects.get(id=id)
    return render(request, 'gallery/show.html', {'card': photo})
