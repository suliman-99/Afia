from Auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'email_verified', 'role', 'first_name', 'last_name', 'phone_number', 'birth_date', 
            'gender',  'photo', 'city', 'blood_type', 'length', 'weight', 'chronic_disease', 'genetic_disease', 'other_info',
            'license', 'available_for_meeting', 'specialization',
        )


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

