from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError
from Auth.serializers import *
from static.serializers import *
from consultation.models import *




class SmallConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'specialization_id', 'doctor_id', 'symptoms', 'additional_explanation', 'analysis', 'done',
                  'specialization', 'patient', 'doctor']
        extra_kwargs = {
            'done': { 'read_only':True  },
            'doctor_id': { 'required': True },
            'specialization_id': { 'required': True },
            'symptoms': { 'required': True },
            'additional_explanation': { 'required': False },
            'analysis': { 'required': False },
        }
        
    specialization_id = serializers.CharField(write_only=True)
    doctor_id = serializers.CharField(write_only=True)

    specialization = SpecializationSerializer(read_only=True)
    patient = UserSerializer(read_only=True)
    doctor = UserSerializer(read_only=True)

    def validate(self, attrs):

        try:
            user = User.objects.get(id=attrs.pop('doctor_id'))
            if user.role != User.ROLE_DOCTOR:
                raise ValidationError({'doctor_id': 'this is not a doctor id'})
            attrs['doctor'] = user
        except User.DoesNotExist:
            raise NotFound('The Doctor you specified is not exist!')
        
        try:
            specialization = Specialization.objects.get(id=attrs.pop('specialization_id'))
            attrs['specialization'] = specialization
        except Specialization.DoesNotExist:
            raise NotFound('The specialization you specified is not exist!')
        
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['patient'] = self.context['request'].user
        print(validated_data)
        return super().create(validated_data)


