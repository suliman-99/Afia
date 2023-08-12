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
    filter_backends = AppointmentOwnerFilterBackend

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        res['count'] = count
        return res

