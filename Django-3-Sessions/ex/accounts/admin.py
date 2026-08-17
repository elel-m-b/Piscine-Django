from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Reputation', {'fields': ('reputation',)}),
    )
    list_display = ('username', 'email', 'reputation', 'is_staff')


admin.site.register(User, UserAdmin)
