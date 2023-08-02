from rest_framework import serializers
from static.serializers import *
from Auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'email_verified', 'role', 'first_name', 'last_name', 'phone_number', 'birth_date', 
            'gender',  'photo', 'blood_type', 'length', 'weight', 'chronic_disease', 'genetic_disease', 'other_info',
            'license', 'available_for_meeting', 'city', 'specialization',
        )
        
    city = CitySerializer()
    specialization = SpecializationSerializer()


def unverified_user_response(user):
    return {
        'user': UserSerializer(user).data,
    }
    

def verified_user_response(user, refresh, access):
    return {
        'user': UserSerializer(user).data,
        'refresh': refresh,
        'access': access,
    }

