from rest_framework import serializers
from Auth.response_templates import UserSerializer
from appointment.models import *


class GetAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'status', 'date', 'time', 'patient_notes', 'doctor_notes', 'doctor']

    doctor = UserSerializer()


class PatientCreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'patient_notes']

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data


class DoctorAcceptAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['time', 'doctor_notes']

    def update(self, instance, validated_data):
        validated_data['status'] = Appointment.STATUS_ACCEPTED
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data


class DoctorRejectAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'doctor_notes']

    def update(self, instance, validated_data):
        validated_data['status'] = Appointment.STATUS_REJECTED
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data


class PatientConfirmAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = []

    def update(self, instance, validated_data):
        validated_data['status'] = Appointment.STATUS_CONFIRMED
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data


class PatientCancelAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = []

    def update(self, instance, validated_data):
        validated_data['status'] = Appointment.STATUS_CANCELED
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data
    
