from django.contrib import admin
from .models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ('priority',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Task, TaskAdmin)
