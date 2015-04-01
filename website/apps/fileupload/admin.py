from django.contrib import admin

from fileupload.models import File

class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('file_tag',)
    list_display = ('file', 'file_tag_thumb', 'created')


admin.site.register(File, FileAdmin)
