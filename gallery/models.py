from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image_url = models.CharField(max_length=255, null=False, blank=False)
    # image = models.ImageField(upload_to='photos/', null=False, blank=False)

    def __str__(self):
        return f'Photo:{self.name} from {self.description}'
