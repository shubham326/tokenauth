from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(message)
class messageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'created_at', 'updated_at', 'created_by']
