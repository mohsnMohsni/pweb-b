# Core imports.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import (
    UserAdmin as CoreUserAdmin,
    GroupAdmin as CoreGroupAdmin,
)
from django.contrib.auth.models import Group, Permission

from .models import User


admin.site.unregister(Group)
admin.site.empty_value_display = _('unknown')


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    def __init__(self, model, admin_site):
        model._meta.app_label = 'accounts'
        super().__init__(model, admin_site)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Group)
class GroupAdmin(CoreGroupAdmin):

    def __init__(self, model, admin_site):
        model._meta.app_label = 'accounts'
        super().__init__(model, admin_site)


@admin.register(User)
class UserAdmin(CoreUserAdmin):
    list_display = ('username', 'full_name', 'national_code')
    list_filter = ('is_staff', 'groups')
    search_fields = ('username', 'full_name')
    readonly_fields = ('last_login', 'date_joined')
    autocomplete_fields = ('groups', 'user_permissions',)
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
