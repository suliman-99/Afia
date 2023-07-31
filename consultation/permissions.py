from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class ConsultationPermission(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user in [obj.patient, obj.doctor]:
            return not obj.done
        return False


class ReviewPermission(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user in [obj.consultation.patient, obj.consultation.doctor]:
            return not obj.done
        return False
    
    