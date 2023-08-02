from rest_framework.viewsets import *
from rest_framework.mixins import *
from resources.permissions import *
from Auth.models import User
from consultation.permissions import *
from consultation.serializers import *
from consultation.filters import *


class ConsultationViewSet(ModelViewSet):
    permission_classes = [IsAccepted, IsConsultationOwner, IsNotDoneForUpdate]
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
        count = Consultation.objects.all().count()
        pending_count = Consultation.objects.filter(done=False).count()
        have_pending_review_count = Consultation.objects.filter(reviews__done=False).count()
        data = ret.data
        ret.data = {}
        ret.data['count'] = count
        ret.data['pending_count'] = pending_count
        ret.data['have_pending_review_count'] = have_pending_review_count
        ret.data['data'] = data
        return ret


class ReviewViewSet(ModelViewSet):
    permission_classes = [IsAccepted, IsReviewOwner, IsNotDoneForUpdate]
    filter_backends = [ReviewOwnerFilterBackend]
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
        count = Review.objects.all().count()
        pending_count = Review.objects.filter(done=False).count()
        data = ret.data
        ret.data = {}
        ret.data['count'] = count
        ret.data['pending_count'] = pending_count
        ret.data['data'] = data
        return ret

