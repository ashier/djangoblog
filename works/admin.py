from django.contrib import admin
from works.models import Project, Media, Category


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slug',)
    list_filter = ('categories',)
    search_fields = ('title', 'markdown_content',)

    fieldsets = [
        ('Projects', {
            'fields': ('title', 'sub_title', )
        }),
        ('DownloadUrl, Project Website and Project Location', {
            'fields': ('url', 'website', 'location',)
        }),
        ('Markdown', {
            'fields': ('markdown_content', )
        }),
        ('Type & Categories', {
            'fields': ('type', 'categories', )
        }),
        ('Related Media', {
            'fields': ('medium', )
        }),
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Media)
