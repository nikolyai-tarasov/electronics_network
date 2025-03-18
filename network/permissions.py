from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """Определения активного пользователя"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)
