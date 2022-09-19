from django.contrib import admin
from .models import Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug')
    prepopulated_fields = {'slug':('tag_name',)}

admin.site.register(Tag, TagAdmin)
