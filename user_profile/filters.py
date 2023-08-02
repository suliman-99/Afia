from rest_framework.filters import BaseFilterBackend


class DoctorFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        consultation_id = request.query_params.get('consultation_id')
        if consultation_id:
            queryset = queryset.filter(consultation_id=consultation_id)
        return queryset
    
    