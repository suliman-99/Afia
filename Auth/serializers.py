import datetime
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
        return user_dict(instance)


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        ret = super().validate(attrs)
        if not self.user.email_verified:
            return user_dict(self.user)
        return verified_user_dict(self.user, ret['refresh'], ret['access'])
        

class SendVerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def update(self, user:User, validated_data):
        user.send_verification_code_email_message()
        return user

    def to_representation(self, user:User):
        return success_response(user_dict(user), message='Code sent! Please check your inbox')
    

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
            raise ValidationError('Send a code before verifying it')

        if datetime.datetime.now(datetime.timezone.utc) - email_code_time > datetime.timedelta(seconds=300):
            raise ValidationError('Old code')

        if not check_password(data.pop('email_code'), email_code):
            raise ValidationError('Wrong code')
        
        user.verify_email()
        refresh = RefreshToken.for_user(user)
        return verified_user_dict(user, str(refresh), str(refresh.access_token))


# class RefreshSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['refresh', 'data']

#     data = UserDataSerializer()
    
#     def validate(self, attrs):
#         try:
#             data = super().validate(attrs)

#             user:User = self.instance

#             if user.refresh == data['refresh']:
#                 return data
#         except:
#             pass
#         raise InvalidToken()
    
#     def update(self, user:User, validated_data):
#         user.update_tokens()
#         validated_data.pop('refresh')

#         user_data = UserData.objects.get_or_create(user=user)[0]
#         serializer = UserDataSerializer(user_data, validated_data['data'])
#         serializer.is_valid()
#         serializer.save()

#         return user

#     def to_representation(self, user:User):
#         return login_response(user, True)


# class ResetPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['password']

#     def update(self, user:User, validated_data):
#         user.set_password(validated_data['password'])
#         user.save()
#         user.update_tokens()
#         return user
    
#     def to_representation(self, user:User):
#         return login_response(user, True)


# class ChagnePasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['old_password', 'password']
    
#     old_password = serializers.CharField(allow_blank=True)

#     def validate(self, attrs):
#         data =  super().validate(attrs)

#         user:User = self.instance

#         old_password = data['old_password']
#         user_password = user.password

#         if user_password:
#             if not check_password(old_password, user_password):
#                 raise ValidationError()
#         else:
#             if old_password:
#                 raise ValidationError()
        
#         return data

#     def update(self, user:User, validated_data):
#         user.set_password(validated_data['password'])
#         if user.signup_type in get_choices_values(User.SIGNUP_TYPE_SOCIAL_CHOICES) and user.email:
#             user.verify_email()
#         user.save()
#         user.update_tokens()
#         return user
    
#     def to_representation(self, user:User):
#         return login_response(user, True)


# class ChangeEmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']
#         extra_kwargs = {
#             'email': {'required': True},
#         }

#     def update(self, user:User, validated_data):
#         user.change_email(validated_data['email'])
#         user.send_verification_code_email_message()
#         user.update_tokens()
#         return user
    
#     def to_representation(self, user:User):
#         return login_response(user, False)

