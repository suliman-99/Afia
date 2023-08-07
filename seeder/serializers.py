from rest_framework import serializers
from statics.models import *
from Auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 
            'password', 
            'is_staff', 
            'is_superuser', 
            'accepted',
            'role',
            'first_name', 
            'last_name', 
            'phone_number', 
            'birth_date', 
            'gender', 
            'available_for_meeting', 
            'blood_type',
            'length', 
            'weight',
            'chronic_disease',
            'genetic_disease',
            'other_info',
        ]
        extra_kwargs = {
            'first_name': { 'required': False },
            'last_name': { 'required': False },
            'phone_number': { 'required': False },
            'birth_date': { 'required': False },
            'gender': { 'required': False },
            'available_for_meeting': { 'required': False },
            'blood_type': { 'required': False },
            'length': { 'required': False },
            'weight': { 'required': False },
            'chronic_disease': { 'required': False },
            'genetic_disease': { 'required': False },
            'other_info': { 'required': False },
            'accepted': { 'required': False },
            'role': { 'required': False },
        }


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

