from gallery.models import Photo


def populate_gallery():
    """
    Populate the gallery with the following photos:
    To run this script, use the following command:
    python manage.py shell < utils/populate_gallery.py
    """
    photo1 = Photo(name='Galáxia NGC 1079', author='webbtelescope.org / NASA / Hubble',
                   description='A Galáxia de Andromeda é uma das mais famosas galáxias do universo. Ela é uma galáxia espiral.', image_url='hubble_ngc1079.jpg')
    photo1.save()
    photo2 = Photo(name='Galáxia de Olho Negro', author='webbtelescope.org / NASA / Hubble',
                   description='A Galáxia de Olho Negro é uma das mais famosas galáxias do universo. Ela é uma galáxia elíptica.', image_url='cartwheel-galaxy.png')
    photo2.save()

    Photo.objects.all().count()
