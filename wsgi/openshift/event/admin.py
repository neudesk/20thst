from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('__str__',
                    'post_type',
                    'admin_thumbnail',
                    'start_date',
                    'end_date',
                    'is_pub'
                    )
    admin_thumbnail = AdminThumbnail(image_field='cover_thumbnail')
    
admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory)
admin.site.register(PostType)