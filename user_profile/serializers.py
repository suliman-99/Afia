from rest_framework import serializers
from statics.serializers import *
from Auth.models import User
from Auth.response_templates import *


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
            'first_name': {'required': True, 'allow_null':False, 'allow_blank':False},
            'last_name': {'required': True, 'allow_null':False, 'allow_blank':False},
            'phone_number': {'required': True, 'allow_null':False, 'allow_blank':False},
            'birth_date': {'required': True, 'allow_null':False},
            'gender': {'required': True, 'allow_null':False},
            'photo': {'required': False},
            'city_id': {'required': True},
            'blood_type': {'required': True, 'allow_null':False},
            'length': {'required': True, 'allow_null':False},
            'weight': {'required': True, 'allow_null':False},
            'chronic_disease': {'required': False},
            'genetic_disease': {'required': False},
            'other_info': {'required': False},
        }
        
    city_id = serializers.IntegerField(write_only=True, allow_null=False)
    
    def to_representation(self, user:User):
        return UserSerializer(user).data


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
            'specialization_id',
        ]
        
        extra_kwargs = {
            'first_name': {'required': True, 'allow_null':False, 'allow_blank':False},
            'last_name': {'required': True, 'allow_null':False, 'allow_blank':False},
            'phone_number': {'required': True, 'allow_null':False, 'allow_blank':False},
            'birth_date': {'required': True, 'allow_null':False},
            'gender': {'required': True, 'allow_null':False},
            'photo': {'required': False},
            'city_id': {'required': True, 'allow_null':False},
            
            'license': {'required': True, 'allow_null':False},
            'available_for_meeting': {'required': True, 'allow_null':False},
            'specialization_id': {'required': True, 'allow_null':False},
        }
        
    city_id = serializers.IntegerField(write_only=True, allow_null=False)
    specialization_id = serializers.IntegerField(write_only=True, allow_null=False)
    
    def to_representation(self, user:User):
        return UserSerializer(user).data
    
