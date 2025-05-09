from django.contrib import admin
from forum.models import Post, Section, Thread
from core.admin import TimeStampModelAdmin

   

class PostModelAdmin(TimeStampModelAdmin):
    model = Post
    list_display = ['author', 'id', 'created', 'modified']
    

class SectionModelAdmin(TimeStampModelAdmin):
    model = Section
    list_display = ['name', 'id', 'created', 'modified']
   

class ThreadModelAdmin(TimeStampModelAdmin):
    model = Thread
    list_display = ['title', 'id', 'created', 'modified']
    list_filter = ['section']

admin.site.register(Post, PostModelAdmin)
admin.site.register(Section, SectionModelAdmin)
admin.site.register(Thread, ThreadModelAdmin)  