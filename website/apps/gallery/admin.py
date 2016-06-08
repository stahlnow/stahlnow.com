from django.contrib import admin

from gallery.models import Gallery, Image


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('image', 'image_tag', 'gallery', 'created')
    ordering = ('gallery', 'created')


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery)