from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role == 'staff'


class IsUserProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id


class IsUserProfileOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.id:
            return True
        return request.user.is_superuser

#==========================================