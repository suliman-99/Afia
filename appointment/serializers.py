from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from Auth.response_templates import UserSerializer
from appointment.models import *


class GetAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'status', 'date', 'time', 'patient_notes', 'doctor_notes', 'doctor', 'patient']

    doctor = UserSerializer()
    patient = UserSerializer()


class PatientCreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'patient_notes', 'doctor_id']
        extra_kwargs = {
            'date': { 'required': True }
        }

    doctor_id = serializers.CharField(required=True)

    def create(self, validated_data):
        validated_data['patient'] = self.context['request'].user
        validated_data['doctor'] = get_object_or_404(User, id=validated_data['doctor_id'])
        return super().create(validated_data)

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data


class DoctorAcceptAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['time', 'doctor_notes']
        extra_kwargs = {
            'time': { 'required': True }
        }

    def update(self, instance, validated_data):
        validated_data['status'] = Appointment.STATUS_ACCEPTED
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data


class DoctorRejectAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'doctor_notes']
        extra_kwargs = {
            'date': { 'required': True }
        }

    def update(self, instance, validated_data):
        validated_data['status'] = Appointment.STATUS_REJECTED
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return GetAppointmentSerializer(instance, context=self.context).data


class PatientRequestAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'patient_notes']
        extra_kwargs = {
            'date': { 'required': True }
        }

    def update(self, instance, validated_data):
        validated_data['status'] = Appointment.STATUS_REQUESTED
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
    
