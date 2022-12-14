import imp
from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title','tag','publish_date','published')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username','created_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)