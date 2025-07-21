from django.contrib import admin
from .models import Photo


class ListPhoto(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'image_url')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'author', 'description')
    list_filter = ('author', 'description')
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('author', 'image_url')


admin.site.register(Photo, ListPhoto)
