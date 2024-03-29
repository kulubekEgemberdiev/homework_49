from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from accounts.models import Profile


class ProfileAdmin(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileAdmin,)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)