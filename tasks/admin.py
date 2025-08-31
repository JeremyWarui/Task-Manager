from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    """
    Class that defines how tasks will be displayed in the Admin
    """
    list_display = ('title', 'description', 'status', 'created_at', 'user')
    list_filter = ['status']
    search_fields = ('title', 'status', 'description')