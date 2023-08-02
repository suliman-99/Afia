from rest_framework.filters import BaseFilterBackend
from Auth.models import User


class ConsultationOwnerFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.role == User.ROLE_PATIENT:
            return queryset.filter(patient=request.user)
        if request.user.role == User.ROLE_DOCTOR:
            return queryset.filter(docotr=request.user)
        return None


class ReviewOwnerFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.role == User.ROLE_PATIENT:
            return queryset.filter(consultation__patient=request.user)
        if request.user.role == User.ROLE_DOCTOR:
            return queryset.filter(consultation__docotr=request.user)
        return None


class ReviewConsultationFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        consultation_id = request.query_params.get('consultation_id')
        if consultation_id:
            queryset = queryset.filter(consultation_id=consultation_id)
        return queryset
        
    
