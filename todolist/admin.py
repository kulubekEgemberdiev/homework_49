from django.contrib import admin

# Register your models here.
from todolist.models import TodolistModel, Statuses, Types


class TypesAdminInline(admin.TabularInline):
    model = TodolistModel.types.through


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_date']
    list_display_links = ['summary']
    list_filter = ['summary']
    search_fields = ['summary']
    fields = ['summary', 'description', 'status', 'created_date', 'updated_date']
    readonly_fields = ['created_date', 'updated_date']
    inlines = [TypesAdminInline]


class StatusesAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_display_links = ['status']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status']


class TypesAdmin(admin.ModelAdmin):
    inlines = [TypesAdminInline]


admin.site.register(TodolistModel, TodoAdmin)
admin.site.register(Statuses, StatusesAdmin)
admin.site.register(Types, TypesAdmin)
