from rest_framework import serializers
from statics.models import *
from Auth.models import User


class SuperuserSeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class DoctorSeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 
            'password', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'birth_date', 
            'gender', 
            'available_for_meeting', 
        ]

    def create(self, validated_data):
        validated_data['role'] = User.ROLE_DOCTOR
        validated_data['accepted'] = True
        return User.objects.create_user(**validated_data)


class PatientSeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 
            'password', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'birth_date', 
            'gender', 
            'blood_type',
            'length', 
            'weight',
            'chronic_disease',
            'genetic_disease',
            'other_info',
        ]

    def create(self, validated_data):
        validated_data['role'] = User.ROLE_PATIENT
        return User.objects.create_user(**validated_data)

