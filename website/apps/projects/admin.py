from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from projects.models import Project, Category

from fileupload.models import File

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)

class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'category', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    change_form_template = 'projects/admin/change_form.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id

        return super(ProjectAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'teaser', 'tags')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'category', 'status', 'allow_comments', 'author', 'publish')
        }),

    )

admin.site.register(Project, ProjectAdmin)