from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework_simplejwt.views import TokenObtainPairView
from Auth.serializers import *


class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = ()


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer
    permission_classes = ()


class SendVerificationCodeView(UpdateAPIView):
    serializer_class = SendVerificationCodeSerializer
    permission_classes = ()

    def get_object(self):
        email = self.request.data.get('email')
        if not email:
            raise ValidationError({'email': 'This field is required.'})
        return get_object_or_404(User, email=self.request.data.get('email'))


class VerifyView(UpdateAPIView):
    serializer_class = VerifySerializer
    permission_classes = ()

    def get_object(self):
        email = self.request.data.get('email')
        if not email:
            raise ValidationError({'email': 'This field is required.'})
        return get_object_or_404(User, email=self.request.data.get('email'))

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
        

class RefreshView(CreateAPIView):
    serializer_class = RefreshSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ResetPasswordView(UpdateAPIView):
    serializer_class = ResetPasswordSerializer

    def get_object(self):
        return self.request.user
    

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChagnePasswordSerializer

    def get_object(self):
        return self.request.user


class ChangeEmailView(UpdateAPIView):
    serializer_class = ChangeEmailSerializer

    def get_object(self):
        return self.request.user

