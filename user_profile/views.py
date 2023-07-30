from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from user_profile.serializers import *


class PatientProfileViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = PatientProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return self.request.user


class DoctorProfileViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return self.request.user

