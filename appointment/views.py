from rest_framework.generics import CreateAPIView, UpdateAPIView
from appointment.serializers import *


class PatientCreateAppointmentView(CreateAPIView):
    serializer_class = PatientCreateAppointmentSerializer


class DoctorAcceptAppointmentView(UpdateAPIView):
    serializer_class = DoctorAcceptAppointmentSerializer
    queryset = Appointment.objects.all()


class DoctorRejectAppointmentView(UpdateAPIView):
    serializer_class = DoctorRejectAppointmentSerializer
    queryset = Appointment.objects.all()


class PatientConfirmAppointmentView(UpdateAPIView):
    serializer_class = PatientConfirmAppointmentSerializer
    queryset = Appointment.objects.all()


class PatientCancelAppointmentView(UpdateAPIView):
    serializer_class = PatientCancelAppointmentSerializer
    queryset = Appointment.objects.all()

