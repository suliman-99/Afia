from resources.permissions import BasePermission
from Auth.models import User

class IsConsultationOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == User.ROLE_PATIENT and request.user == obj.patient \
        or request.user.role == User.ROLE_DOCTOR and request.user == obj.doctor


class IsReviewOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == User.ROLE_PATIENT and request.user == obj.consultation.patient \
        or request.user.role == User.ROLE_DOCTOR and request.user == obj.consultation.doctor
    
    
class IsNotDoneForUpdate(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not (request.method in ['PUT', 'PATCH'] and obj.done)

