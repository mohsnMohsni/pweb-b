# Core imports.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import (
    UserAdmin as CoreUserAdmin,
    GroupAdmin as CoreGroupAdmin,
)
from django.contrib.auth.models import Group, Permission

from .models import User, VerificationCodeModel


admin.site.unregister(Group)
admin.site.empty_value_display = _('unknown')


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(Group)
class GroupAdmin(CoreGroupAdmin):
    autocomplete_fields = ('permissions',)


@admin.register(User)
class UserAdmin(CoreUserAdmin):
    list_display = ('username', 'full_name', 'national_code')
    list_filter = ('is_staff', 'groups')
    search_fields = ('username', 'full_name')
    readonly_fields = ('last_login', 'date_joined')
    autocomplete_fields = ('groups', 'user_permissions')
    fieldsets = (
        (
            _('Auth'),
            {
                'classes': ('collapse',),
                'fields': ('username', 'password'),
            },
        ),
        (
            _('Profile'),
            {
                'fields': (
                    'national_code',
                    'first_name',
                    'last_name',
                    'birthdate',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_superuser',
                    'is_staff',
                    'is_active',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            _('Actions dates'),
            {
                'fields': ('last_login', 'date_joined'),
            },
        ),
    )


@admin.register(VerificationCodeModel)
class VerificationCodeModelAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code')
    search_fields = ('phone_number',)
    readonly_fields = ('ip',)
