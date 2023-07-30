from rest_framework import serializers
from static.serializers import *
from Auth.models import User
from Auth.response_templates import unverified_user_response


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birth_date',
            'gender',
            'photo',
            'city_id',

            'blood_type',
            'length',
            'weight',
            'chronic_disease',
            'genetic_disease',
            'other_info',

            ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            'birth_date': {'required': True},
            'gender': {'required': True},
            'photo': {'required': False},
            'city_id': {'required': True},
            'blood_type': {'required': True},
            'length': {'required': True},
            'weight': {'required': True},
            'chronic_disease': {'required': False},
            'genetic_disease': {'required': False},
            'other_info': {'required': False},
        }
        
    city_id = serializers.IntegerField(write_only=True)
    
    def to_representation(self, user:User):
        return unverified_user_response(user)


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birth_date',
            'gender',
            'photo',
            'city_id',

            'license',
            'available_for_meeting',
            'specialization',
            
            ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            'birth_date': {'required': True},
            'gender': {'required': True},
            'photo': {'required': False},
            'city_id': {'required': True},
            
            'license': {'required': True},
            'available_for_meeting': {'required': True},
            'specialization': {'required': True},
        }
    
    def to_representation(self, user:User):
        return unverified_user_response(user)
    
