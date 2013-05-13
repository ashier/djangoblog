from django.contrib import admin
from works.models import Project, Media, Category


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slug',)

    fieldsets = [
        ('Projects', {
            'fields': ('title', 'sub_title', 'content', 'categories', 'medium',)
        }),
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Media)
