# Third-party imports.
from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    """
    Custom Permission.
    """

    message = 'You don\'t have permission to access.'

    def has_permission(self, request, view) -> bool:
        return True
