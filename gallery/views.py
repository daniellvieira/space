from django.shortcuts import render

def index(request):
    return render(request, 'gallery/index.html')


def show(request):
    return render(request, 'gallery/show.html')