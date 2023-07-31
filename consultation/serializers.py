from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError
from Auth.serializers import *
from static.serializers import *
from consultation.models import *


class GetConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'symptoms', 'additional_explanation', 
                  'analysis','created_at', 'done',
                  'patient', 'doctor']
        
    patient = UserSerializer()
    doctor = UserSerializer()


class CreateConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'doctor_id', 'symptoms', 'additional_explanation', 'analysis']
        extra_kwargs = {
            'doctor_id': { 'required': True , 'allow_null':False, 'allow_blank':False},
            'symptoms': { 'required': True , 'allow_null':False, 'allow_blank':False},
            'additional_explanation': { 'required': False },
            'analysis': { 'required': False },
        }
        
    doctor_id = serializers.CharField(write_only=True)

    def validate(self, attrs):
        try:
            user = User.objects.get(id=attrs.pop('doctor_id'))
            if user.role != User.ROLE_DOCTOR:
                raise ValidationError({'doctor_id': 'this is not a doctor id'})
            attrs['doctor'] = user
        except User.DoesNotExist:
            raise NotFound('The Doctor you specified is not exist!')
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['patient'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        return GetConsultationSerializer(instance).data


class PatientUpdateConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'symptoms', 'additional_explanation', 'analysis']
        extra_kwargs = {
            'symptoms': { 'required': True , 'allow_null':False, 'allow_blank':False},
            'additional_explanation': { 'required': False },
            'analysis': { 'required': False },
        }
    
    def to_representation(self, instance):
        return GetConsultationSerializer(instance).data

class DoctorUpdateConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'diagnosis', 'prescription', 'treatment_duration']
        extra_kwargs = {
            'diagnosis': { 'required': True, 'allow_null':False, 'allow_blank':False},
            'prescription': { 'required': True, 'allow_null':False, 'allow_blank':False},
            'treatment_duration': { 'required': True, 'allow_null':False, 'allow_blank':False},
        }
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # TODO: make it done when the data needed is filled as saeed need
        if instance:
            instance.done = True
            instance.save()
        return instance
    
    def to_representation(self, instance):
        return GetConsultationSerializer(instance).data



class GetReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_reasons', 'additional_explanation', 'analysis', 'created_at', 'done',
                  'requester', 'consultation']
        
    consultation = GetConsultationSerializer()


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'consultation_id', 'review_reasons', 'additional_explanation', 'analysis']
        extra_kwargs = {
            'consultation_id': { 'required': True, 'allow_null':False, 'allow_blank':False },
            'review_reasons': { 'required': True, 'allow_null':False, 'allow_blank':False },
            'additional_explanation': { 'required': False },
            'analysis': { 'required': False },
        }
        
    consultation_id = serializers.CharField(write_only=True)

    def validate(self, attrs):
        
        try:
            consultation = Consultation.objects.get(id=attrs.pop('consultation_id'))
            attrs['consultation'] = consultation
        except Consultation.DoesNotExist:
            raise NotFound('The consultation you specified is not exist!')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        consultation = validated_data['consultation']
        if consultation.patient == self.context['request'].user:
            validated_data['requester'] = Review.REQUESTER_PATIENT
        elif consultation.doctor == self.context['request'].user:
            validated_data['requester'] = Review.REQUESTER_DOCTOR
        return super().create(validated_data)
    
    def to_representation(self, instance):
        return GetReviewSerializer(instance).data


class PatientUpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_reasons', 'additional_explanation', 'analysis']
        extra_kwargs = {
            'review_reasons': { 'required': True , 'allow_null':False, 'allow_blank':False},
            'additional_explanation': { 'required': False },
            'analysis': { 'required': False },
        }
    
    def to_representation(self, instance):
        return GetReviewSerializer(instance).data


class DoctorUpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'diagnosis', 'prescription', 'treatment_duration']
        extra_kwargs = {
            'diagnosis': { 'required': True, 'allow_null':False, 'allow_blank':False},
            'prescription': { 'required': True, 'allow_null':False, 'allow_blank':False},
            'treatment_duration': { 'required': True, 'allow_null':False, 'allow_blank':False},
        }
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # TODO: make it done when the data needed is filled as saeed need
        if instance:
            instance.done = True
            instance.save()
        return instance
    
    
    def to_representation(self, instance):
        return GetReviewSerializer(instance).data

