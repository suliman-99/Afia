from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from resources.permissions import *
from appointment.permissions import *
from appointment.serializers import *
from appointment.filters import *


class PatientCreateAppointmentView(CreateAPIView):
    serializer_class = PatientCreateAppointmentSerializer


class DoctorAcceptAppointmentView(UpdateAPIView):
    serializer_class = DoctorAcceptAppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAccepted, Requested]


class DoctorRejectAppointmentView(UpdateAPIView):
    serializer_class = DoctorRejectAppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAccepted, Requested]


class PatientRequestAppointmentView(UpdateAPIView):
    serializer_class = PatientRequestAppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAccepted, Rejected]


class PatientConfirmAppointmentView(UpdateAPIView):
    serializer_class = PatientConfirmAppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAccepted, Accepted]


class PatientCancelAppointmentView(UpdateAPIView):
    serializer_class = PatientCancelAppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAccepted]


class AppointmentView(ListAPIView):
    serializer_class = GetAppointmentSerializer
    queryset = Appointment.objects.all()
    filter_backends = [AppointmentOwnerFilterBackend]

    def list(self, request, *args, **kwargs):
        ret = super().list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        requested_count = queryset.filter(status=Appointment.STATUS_REQUESTED).count()
        accepted_count = queryset.filter(status=Appointment.STATUS_ACCEPTED).count()
        rejected_count = queryset.filter(status=Appointment.STATUS_REJECTED).count()
        confirmed_count = queryset.filter(status=Appointment.STATUS_CONFIRMED).count()
        canceled_count = queryset.filter(status=Appointment.STATUS_CANCELED).count()
        future_confirmed_count = queryset.filter(status=Appointment.STATUS_CONFIRMED, date__gte=timezone.now()).count()
        data = ret.data
        ret.data = {}
        ret.data['count'] = count
        ret.data['requested_count'] = requested_count
        ret.data['accepted_count'] = accepted_count
        ret.data['rejected_count'] = rejected_count
        ret.data['confirmed_count'] = confirmed_count
        ret.data['canceled_count'] = canceled_count
        ret.data['future_confirmed_count'] = future_confirmed_count
        ret.data['data'] = data
        return ret

