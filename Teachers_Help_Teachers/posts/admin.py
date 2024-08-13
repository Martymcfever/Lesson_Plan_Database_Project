from django.contrib import admin
from .models import Post, Comment

# Register your models here.

## admin.py is where models from models.py are registered to be seen on the admin page of website
# Comment and Post models are registerd 




admin.site.register(Post)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'lesson_plan')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
class PostAdmin(admin.ModelAdmin):
    list_display = ('title')

