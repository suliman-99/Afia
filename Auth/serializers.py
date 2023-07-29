import datetime
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken
from resources.response_templates import success_response
from Auth.response_templates import *


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('role', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'role': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'style': {'input_type': 'password'}, },
        }

    def create(self, validated_data):
        user:User = User.objects.create_user(**validated_data)
        user.send_verification_code_email_message()
        return user
    
    def to_representation(self, instance):
        return unverified_user_response(instance)


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        ret = super().validate(attrs)
        if not self.user.email_verified:
            return unverified_user_response(self.user)
        return verified_user_response(self.user, ret['refresh'], ret['access'])
        

class SendVerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def update(self, user:User, validated_data):
        user.send_verification_code_email_message()
        return user

    def to_representation(self, user:User):
        return success_response(unverified_user_response(user), message='Code sent! Please check your inbox')
    

class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email_code']
    

    def validate(self, attrs):
        data = super().validate(attrs)
        user:User = self.instance

        email_code = user.email_code
        email_code_time = user.email_code_time
        
        if not email_code_time:
            raise ValidationError({'email_code': 'Send a code before verifying it'})

        if datetime.datetime.now(datetime.timezone.utc) - email_code_time > datetime.timedelta(seconds=300):
            raise ValidationError({'email_code': 'Old code'})

        if not check_password(data.pop('email_code'), email_code):
            raise ValidationError({'email_code': 'Wrong code'})
        
        user.verify_email()
        refresh = RefreshToken.for_user(user)
        return verified_user_response(user, str(refresh), str(refresh.access_token))

class RefreshSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh_str = data.get('refresh')

        try:
            refresh_obj = RefreshToken(refresh_str)
        except:
            raise InvalidToken()
        
        try:
            user = User.objects.get(id=refresh_obj.payload.get('user_id'))
        except:
            raise NotFound()
        
        new_refresh_obj = RefreshToken.for_user(user)
        new_refresh_str = str(new_refresh_obj)
        new_access_str = str(new_refresh_obj.access_token)
        return verified_user_response(user, new_refresh_str, new_access_str)



class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

    def update(self, user:User, validated_data):
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def to_representation(self, user:User):
        return unverified_user_response(user)


class ChagnePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['old_password', 'password']
    
    old_password = serializers.CharField(allow_blank=True)

    def validate(self, attrs):
        data =  super().validate(attrs)
        user:User = self.instance

        old_password = data['old_password']
        user_password = user.password
        if not check_password(old_password, user_password):
            raise ValidationError({'old_password': 'Wrong password'})
        
        return data

    def update(self, user:User, validated_data):
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def to_representation(self, user:User):
        return unverified_user_response(user)


class ChangeEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
        extra_kwargs = {
            'email': {'required': True},
        }

    def update(self, user:User, validated_data):
        user.change_email(validated_data['email'])
        user.send_verification_code_email_message()
        return user
    
    def to_representation(self, user:User):
        return unverified_user_response(user)

