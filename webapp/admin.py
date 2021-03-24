from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ('priority',)


admin.site.register(Task, TaskAdmin)
