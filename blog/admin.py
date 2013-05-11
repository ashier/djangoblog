from django.contrib import admin
from blog.models import Post, Category, Page, Media


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created', 'modified',)
    list_filter = ('categories',)
    search_fields = ('title', 'content',)

    fieldsets = [
        ('Post', {
            'fields': ('title', 'content', 'header_image', 'categories',)
        }),
        ('Author', {
            'fields': ('author',)
        }),
        ('History', {
            'classes': ('collapse',),
            'fields': ('created', 'modified',)
        })
    ]

    readonly_fields = ('created', 'modified',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)

    fieldsets = [
        ('Categories', {
            'fields': ('name',)
        }),
    ]


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)

    fieldsets = [
        ('Pages', {
            'fields': ('name', 'content',)
        }),
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Media)
