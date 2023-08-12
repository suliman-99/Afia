from rest_framework.filters import BaseFilterBackend
from Auth.models import User


class AppointmentOwnerFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.role == User.ROLE_PATIENT:
            return queryset.filter(patient=request.user)
        if request.user.role == User.ROLE_DOCTOR:
            return queryset.filter(doctor=request.user)
        return None

