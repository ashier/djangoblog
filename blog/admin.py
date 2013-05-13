from django.contrib import admin
from blog.models import Post, Category, Media


class CategoryInline(admin.StackedInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created', 'modified',)
    list_filter = ('categories',)
    search_fields = ('title', 'markdown_content',)

    fieldsets = [
        ('Post', {
            'fields': ('title', 'markdown_content', 'header_image',)
        }),
        ('Categories', {
            'fields': ('categories',)
        }),
        ('Author', {
            'fields': ('author',)
        }),
        ('History', {
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


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Media)
