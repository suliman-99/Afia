from rest_framework.filters import BaseFilterBackend


class DoctorSpecializationFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        specialization_id = request.query_params.get('specialization_id')
        if specialization_id:
            queryset = queryset.filter(specialization_id=specialization_id)
        return queryset
    
    