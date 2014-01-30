from django.contrib import admin
from .models import *

admin.site.register(Transition)
admin.site.register(Slide)
admin.site.register(DirectionalTransition)
admin.site.register(Easing)
admin.site.register(StyleClass)
admin.site.register(SlideItem)
admin.site.register(SlideItemImage)