from django.utils import timezone
from rest_framework.viewsets import *
from rest_framework.mixins import *
from resources.permissions import *
from Auth.models import User
from consultation.permissions import *
from consultation.serializers import *
from consultation.filters import *


class ConsultationViewSet(ModelViewSet):
    permission_classes = [IsAccepted, IsConsultationOwner, IsNotDoneForPatientUpdate]
    filter_backends = [ConsultationOwnerFilterBackend]
    queryset = Consultation.objects.all() \
        .select_related('patient') \
        .select_related('doctor') \
        
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetConsultationSerializer
        if self.request.method == 'POST':
            return CreateConsultationSerializer
        if self.request.user.role == User.ROLE_PATIENT:
            return PatientUpdateConsultationSerializer
        if self.request.user.role == User.ROLE_DOCTOR:
            return DoctorUpdateConsultationSerializer
        return None

    def list(self, request, *args, **kwargs):
        ret = super().list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        pending_count = queryset.filter(done=False).count()
        need_review_count = queryset.filter(need_review_at__gt=timezone.now()).count()
        data = ret.data
        ret.data = {}
        ret.data['count'] = count
        ret.data['pending_count'] = pending_count
        ret.data['need_review_count'] = need_review_count
        ret.data['data'] = data
        return ret


class ReviewViewSet(ModelViewSet):
    permission_classes = [IsAccepted, IsReviewOwner, IsNotDoneForPatientUpdate]
    filter_backends = [ReviewOwnerFilterBackend, ReviewConsultationFilterBackend]
    queryset = Review.objects.all() \
        .select_related('consultation') \
        
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetReviewSerializer
        if self.request.method == 'POST':
            return CreateReviewSerializer
        if self.request.user.role == User.ROLE_PATIENT:
            return PatientUpdateReviewSerializer
        if self.request.user.role == User.ROLE_DOCTOR:
            return DoctorUpdateReviewSerializer
        return None

    def list(self, request, *args, **kwargs):
        ret = super().list(request, *args, **kwargs)
        queryset = ReviewOwnerFilterBackend().filter_queryset(self.request, self.get_queryset(), self)
        count = queryset.count()
        pending_count = queryset.filter(done=False).count()
        data = ret.data
        ret.data = {}
        ret.data['count'] = count
        ret.data['pending_count'] = pending_count
        ret.data['data'] = data
        return ret

