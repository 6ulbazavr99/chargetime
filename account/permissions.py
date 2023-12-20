from rest_framework import permissions

# rest_framework.


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == 'staff':
            return True
        return False
