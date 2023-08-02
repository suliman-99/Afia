from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAcceptedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.accepted:
            return True
        return False
        
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.accepted:
            return True
        return False
    

class IsAccepted(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.accepted:
            return True
        return False
        
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.accepted:
            return True
        return False

