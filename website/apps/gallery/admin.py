from django.contrib import admin

from gallery.models import Image


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('image', 'image_tag', 'created')


admin.site.register(Image, ImageAdmin)
