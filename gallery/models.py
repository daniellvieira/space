from django.db import models
from django.conf import settings


class CategoryOptions(models.IntegerChoices):
    GALAXY = 1, 'Galáxia'
    PLANET = 2, 'Planeta'
    STAR = 3, 'Estrela'
    OTHER = 4, 'Outro'


class Photo(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image_url = models.CharField(max_length=255, null=False, blank=False)
    category = models.IntegerField(
        choices=CategoryOptions.choices, default=CategoryOptions.OTHER)

    def __str__(self):
        return f'Photo: [{self.get_category_display()}] {self.name} from {self.author}'
