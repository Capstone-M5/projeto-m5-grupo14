from rest_framework import permissions


class IsAdmin_Or_ReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("PATCH", "GET"):
            return bool(request.user and request.user.is_authenticated and obj.user.username == request.user.username)
        return bool(
            (request.user and request.user.is_authenticated and obj.user.username ==
             request.user.username) or request.user.is_superuser
        )
