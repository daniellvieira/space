from re import M
from django.shortcuts import render

data = {
    1: {
        'name': 'Nebulosa Carina',
        'author': 'webbtelescope.org / NASA / James Webb',
        'description': 'A Nebulosa Carina é uma das mais famosas nebulosas do universo. Ela é uma região jovem e próxima de formação de estrelas.',
        'image': 'carina-nebula.png'
    },
    2: {
        'name': 'Galáxia de Andromeda',
        'author': 'webbtelescope.org / NASA / Hubble',
        'description': 'A Galáxia de Andromeda é uma das mais famosas galáxias do universo. Ela é uma galáxia espiral.',
        'image': 'andromeda-galaxy.png'
    },
    3: {
        'name': 'Galáxia de Olho Negro',
        'author': 'webbtelescope.org / NASA / Hubble',
        'description': 'A Galáxia de Olho Negro é uma das mais famosas galáxias do universo. Ela é uma galáxia elíptica.',
        'image': 'black-eye-galaxy.png'
    }
}

def index(request):
    return render(request, 'gallery/index.html', {'cards': data})


def show(request, id):
    return render(request, 'gallery/show.html', {'card': data[id]})