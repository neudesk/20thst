from django.contrib import admin
from .models import *

class AdminToken(admin.ModelAdmin):
    list_display = ("__str__", "user", "created", "expiration")
admin.site.register(Token, AdminToken)