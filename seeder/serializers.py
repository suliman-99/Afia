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
            'photo', 
            'license',
            'available_for_meeting', 
            'city_name', 
            'specialization_name',
        ]

    photo = serializers.CharField()
    city_name = serializers.CharField()
    specialization_name = serializers.CharField()

    def create(self, validated_data):
        validated_data['role'] == User.ROLE_DOCTOR
        validated_data['accepted'] == True
        validated_data['city'] == City.objects.get(name=validated_data.get('city_name'))
        validated_data['specialization'] == Specialization.objects.get(name=validated_data.get('specialization_name'))
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
            'photo', 
            'blood_type',
            'length', 
            'weight',
            'chronic_disease',
            'genetic_disease',
            'other_info',
            'city_name', 
        ]

    photo = serializers.CharField()
    city_name = serializers.CharField()

    def create(self, validated_data):
        validated_data['role'] == User.ROLE_PATIENT
        validated_data['city'] == City.objects.get(name=validated_data.get('city_name'))
        return User.objects.create_user(**validated_data)

