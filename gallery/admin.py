from django.contrib import admin
from .models import Photo


class ListPhoto(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'image_url', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'author', 'description', 'category')
    list_filter = ('author', 'description', 'category')
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('author', 'image_url')


admin.site.register(Photo, ListPhoto)
