from django.contrib import admin


# Register your models here.
from todolist.models import TodolistModel, Statuses, Types


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_date']
    list_display_links = ['summary']
    list_filter = ['summary']
    search_fields = ['summary']
    fields = ['summary', 'description', 'status', 'type', 'created_date', 'updated_date']
    readonly_fields = ['created_date', 'updated_date']


class StatusesAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_display_links = ['status']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_display_links = ['type']
    list_filter = ['type']
    search_fields = ['type']
    fields = ['type']


admin.site.register(TodolistModel, TodoAdmin)
admin.site.register(Statuses, StatusesAdmin)
admin.site.register(Types, TypesAdmin)
