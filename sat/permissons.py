from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
class IsOwner(permissions.BasePermission):
    """
    Allow only owners access to the object
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner ==request.user