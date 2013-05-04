from django.contrib import admin
from blog.models import Post, Category, Reply


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = [
        ('Post', {
            'fields': ('title', 'content', 'categories')
        }),
        ('Author', {
            'classes': ('collapse',),
            'fields': ('author',)
        }),
        ('History', {
            'classes': ('collapse',),
            'fields': ('created', 'modified')
        })
    ]

    readonly_fields = ('created', 'modified')


class CategoryAdmin(admin.ModelAdmin):
    pass


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'website')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reply, ReplyAdmin)

