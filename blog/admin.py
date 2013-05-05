from django.contrib import admin
from blog.models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created', 'modified',)
    list_filter = ('created', 'modified',)
    search_fields = ('title', 'content',)

    fieldsets = [
        ('Post', {
            'fields': ('title', 'content', 'comments_allowed',)
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


class CommentAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'website',)
    fieldsets = [
        ('Comment Fields', {
            'fields': ('post', 'fullname', 'email', 'website', 'message',)
        }),
        ('Flags', {
            'fields': ('is_spam',)
        }),
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
