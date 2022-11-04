from rest_framework import permissions
import ipdb

class IsAuthenticatedOrReadOnlyPersonality(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in "GET" or
            request.user and
            request.user.is_authenticated and request.user.is_superuser
        )