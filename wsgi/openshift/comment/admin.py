from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__',
                    'message')
    
admin.site.register(Comment, CommentAdmin)