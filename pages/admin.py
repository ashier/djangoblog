from django.contrib import admin
from pages.models import Page, Media


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_general',)

    fieldsets = [
        ('Pages', {
            'fields': ('name', 'content', 'is_general',)
        }),
    ]


admin.site.register(Page, PageAdmin)
admin.site.register(Media)
