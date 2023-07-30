from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from consultation.serializers import *


class ConsultationViewSet(ModelViewSet):
    serializer_class = SmallConsultationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Consultation.objects.all() \
        .prefetch_related('patient') \
        .prefetch_related('doctor') \
        .prefetch_related('specialization') \

    def list(self, request, *args, **kwargs):
        ret = super().list(request, *args, **kwargs)
        count = Consultation.objects.filter().count()
        not_done_count = Consultation.objects.filter(done=False).count()
        # have_not_done_review_count = Consultation.objects.filter(done=False).count()
        have_not_done_review_count = 0
        data = ret .data
        ret.data = {}
        ret.data['count'] = count
        ret.data['not_done_count'] = not_done_count
        ret.data['have_not_done_review_count'] = have_not_done_review_count
        ret.data['data'] = data
        return ret

