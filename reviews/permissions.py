from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.username == request.user.username)


class IsAdmin_Or_ReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            obj.username == request.user.username
            or request.user
            and request.user.is_superuser
        )
