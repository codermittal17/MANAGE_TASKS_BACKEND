from django.contrib import admin
from .models import TasksInfo
# Register your models here.

@admin.register(TasksInfo)
class TaskInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'due_date', 'priority_levels', 'status')