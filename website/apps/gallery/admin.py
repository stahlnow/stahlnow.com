from django.contrib import admin

from gallery.models import File


class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('file', 'image_tag', 'created')


admin.site.register(File, FileAdmin)
