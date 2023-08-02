from rest_framework.permissions import BasePermission


class IsAccepted(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.accepted:
            return True
        return False

