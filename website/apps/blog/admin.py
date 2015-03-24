from django.contrib import admin

from blog.models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    change_form_template = 'blog/admin/change_form.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id

        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'tags')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'categories', 'status', 'allow_comments', 'author', 'publish')
        }),

    )

admin.site.register(Post, PostAdmin)